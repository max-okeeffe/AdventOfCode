open Stdio
open Base

let filename = "data.txt"
let data = In_channel.input_all @@ In_channel.create filename

let fish = data |> String.split ~on:',' |> List.map ~f:Int.of_string
let n = 80

let rec fish_produced day timer =
  match day, timer with
  | x, _ when x > n -> 0
  | 0, y -> 1 + fish_produced y 0
  | x, 8 -> 1 + fish_produced (x+8) 0
  | x, _ -> fish_produced (x+1) 8 + fish_produced (x+7) 0

let num = fish |> List.map ~f:(fish_produced 0) |> List.fold ~init:0 ~f:(+)

let () = Stdio.print_endline @@ Int.to_string @@ num
