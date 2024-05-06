let reverse_string s =
  let len = String.length s in
  let result = Bytes.create len in
  for i = 0 to len - 1 do
      Bytes.set result i s.[len - 1 - i]
   done;
   Bytes.to_string result

let reverse_words_in_line line =
  let words = String.split_on_char ' ' line in
  let reversed_words = List.map reverse_string words in
  String.concat " " reversed_words

let rec reverse_words_in_input() =
  try
    let line = input_line stdin in
    let reversed_line = reverse_words_in_line line in
    print_endline reversed_line;
    reverse_words_in_input ()
  with End_of_file -> ()

let () =
  reverse_words_in_input ()
