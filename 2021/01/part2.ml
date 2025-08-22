open Stdio
open Base

let filename = "data.txt"
let data = In_channel.input_all @@ In_channel.create filename

let depths = List.map (String.split data ~on:'\n') ~f:Int.of_string
let n = List.length depths

let sub_list l i k = List.sub l ~pos:i ~len:k

let threes = List.map3_exn (sub_list depths 0 (n-2)) (sub_list depths 1 (n-2)) (sub_list depths 2 (n-2)) ~f:(fun x y z -> x+y+z)
let diffs = List.map2_exn (sub_list threes 0 (n-3)) (sub_list threes 1 (n-3)) ~f:(-)
let count = List.length @@ List.filter diffs ~f:(fun x -> x < 0)

let () = Stdio.print_endline @@ Int.to_string count
