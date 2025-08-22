open Stdio
open Base

let filename = "data.txt"
let data = In_channel.input_all @@ In_channel.create filename

let moves = List.map (String.split data ~on:'\n') ~f:(fun s -> String.split s ~on: ' ')

let rec make l x y aim = match l with
  | [] -> x * y
  | move :: t -> match move with
    | ["forward"; n] -> make t (x + Int.of_string n) (y + aim * Int.of_string n) aim
    | ["up"; n] -> make t x y (aim - Int.of_string n)
    | ["down"; n] -> make t x y (aim + Int.of_string n)
    | _ -> 0

let () = Stdio.print_endline @@ Int.to_string @@ make moves 0 0 0
