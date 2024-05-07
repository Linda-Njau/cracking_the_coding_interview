let rec reverse_string s =
  let words = String.split_on_char ' ' s in
  let reversed_words = List.map(fun word -> 
    let len = String.length word in
    let result = Bytes.create len in
    for i = 0 to len - 1 do
      Bytes.set result i word.[len - 1 - i]
    done;
    Bytes.to_string result
  ) words in
  String.concat " " reversed_words

let reverse_lines lines =
  List.map reverse_string lines

let read_input ?(file_path="") () =
  let split_into_words line =
    let pattern = Str.regexp "[ \t\n,.!?]+" in
    Str.full_split pattern line
    |> List.filter_map (function
      | Str.Text s -> Some s
      | Str.Delim _ -> None)
  in
  let read_from_terminal () =
    let rec read_lines acc =
      try
        let line = input_line stdin in
        read_lines (line :: acc)
      with End_of_file -> List.rev acc
    in
    read_lines []
  in
  let rec tokenize_line line =
    let rec tokenize_char acc = function
      | '\t' -> "%%" :: acc  (* Tokenize tabs as "%%" *)
      | '\n' -> "*" :: acc   (* Tokenize newlines as "*" *)
      | ' ' -> "&" :: acc    (* Tokenize spaces as "&" *)
      | c -> String.make 1 c :: acc
    in
    String.to_seq line
    |> Seq.fold_left tokenize_char []
    |> List.rev
    |> String.concat ""
  in 
  let read_from_file file_path =
    let channel = open_in file_path in
    let rec read_lines acc =
      try
        let line = input_line channel in
        print_endline (tokenize_line line);
        read_lines (line :: acc)
      with End_of_file ->
        close_in channel;
        List.rev acc
    in
    read_lines []
  in
  match file_path with
  | "" -> read_from_terminal ()
  | _ -> List.flatten (List.map split_into_words (read_from_file file_path))

let reverse_words_in_paragraph paragraph =
  let words = String.split_on_char ' ' paragraph in
  let reversed_words = List.map reverse_string words in
  String.concat " " (List.rev reversed_words)

let process_input ?file_path () =
  let input_lines =
    match file_path with
    | Some path -> read_input ~file_path:path ()
    | None -> read_input ()
  in
  let reversed_lines = reverse_lines input_lines in
  List.iter (fun line -> print_endline line) reversed_lines

let () =
  if Array.length Sys.argv > 1 then (
    let file_path = Sys.argv.(1) in
    process_input ~file_path:file_path ()
  ) else (
    process_input ()
  )
