
let rec reverse_string s =
  let words = String.split_on_char ' ' s in
  List.iter (fun word -> print_endline ("Original word: " ^ word)) words;  (* Print original words *)
  let reversed_words = List.map (fun word ->
    let pattern = Str.regexp "[^a-zA-Z0-9\\p{Punct}]" in
    let cleaned_word = Str.global_replace pattern "" word in
      let len = String.length cleaned_word in
      let result = Bytes.create len in
      for i = 0 to len - 1 do
        Bytes.set result i cleaned_word.[len - 1 - i];
        print_endline ("Reversing character: " ^ String.make 1 word.[len - 1 - i]);  (* Print reversed character *)
        done;
      Bytes.to_string result
  ) words in
  List.iter (fun word -> print_endline ("Reversed word: " ^ word)) reversed_words;  (* Print reversed words *)
  String.concat " " reversed_words


let reverse_lines lines =
  List.map reverse_string lines

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
  let reversed_lines = reverse_lines input_lines in
  List.iter (fun line -> print_endline line) reversed_lines

let () =
  if Array.length Sys.argv > 1 then (
    let file_path = Sys.argv.(1) in
    process_input ~file_path:file_path ()
  ) else (
    process_input ()
  )
