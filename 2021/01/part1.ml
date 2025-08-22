open Stdio
open Base

let filename = "data.txt"
let data = In_channel.input_all @@ In_channel.create filename

let depths = List.map (String.split data ~on:'\n') ~f:Int.of_string
let n = List.length depths

let diffs = List.map2_exn (List.sub depths ~pos:0 ~len:(n-1)) (List.sub depths ~pos:1 ~len:(n-1)) ~f:(-)
let count = List.length @@ List.filter diffs ~f:(fun x -> x < 0)

let () = Stdio.print_endline @@ Int.to_string count
