let rec reverse_word word =
  let cleaned_word = 
    String.concat "" (List.filter_map (fun c ->
      if (Char.code c) >= 32 && (Char.code c) <= 126 && (Char.code c) != 13 then Some (String.make 1 c)
      else None) (String.to_seq word |> List.of_seq))
  in
  let len = String.length cleaned_word in
  let result = Bytes.create len in
  for i = 0 to len - 1 do
    Bytes.set result i cleaned_word.[len - 1 - i]
  done;
  Bytes.to_string result

let reverse_line s =
  let words = String.split_on_char ' ' s in
  let reversed_words = List.map reverse_word words in
  String.concat " " reversed_words

let reverse_multiple_lines lines =
  List.map reverse_line lines

let read_input ?(file_path="") () =
  let read_from_terminal () =
    let rec read_lines acc =
      try
        let line = input_line stdin in
        read_lines (line :: acc)
      with End_of_file -> List.rev acc
    in
    read_lines []
  in
  let read_from_file file_path =
    let channel = open_in file_path in
    let rec read_lines acc =
      try
        let line = input_line channel in
        read_lines (line :: acc)
      with End_of_file ->
        close_in channel;
        List.rev acc
    in
    read_lines []
  in
  match file_path with
  | "" -> read_from_terminal ()
  | _ -> read_from_file file_path

let process_input ?file_path () =
  let input_lines =
    match file_path with
    | Some path -> read_input ~file_path:path ()
    | None -> read_input ()
  in
  let reversed_lines = reverse_multiple_lines input_lines in
  List.iter print_endline reversed_lines

let () =
  if Array.length Sys.argv > 1 then (
    let file_path = Sys.argv.(1) in
    process_input ~file_path:file_path ()
  ) else (
    process_input ()
  )
