open Stdio
open Base

let filename = "data.txt"
let data = In_channel.input_all @@ In_channel.create filename

let split_list l =
  let n = List.length l in
  let rec aux out curr i =
    if i = n then out @ [curr]
    else let x = List.nth_exn l i in
    if not @@ String.equal x "" then aux out (curr @ [x]) (i+1)
    else aux (out @ [curr]) [] (i+1) in
  aux [] [] 0

let elves = split_list @@ String.split data ~on:'\n'

let elf_sum (l : string list) = List.fold (List.map l ~f:Int.of_string) ~init:0 ~f:(+)

let get_max =
  let n = List.length elves in
  let rec aux maxval i =
    if i = n then maxval
    else let curr = elf_sum @@ List.nth_exn elves i in
    if curr > maxval then aux curr (i+1) else aux maxval (i+1) in
  aux 0 0

let () = Stdio.print_endline @@ Int.to_string get_max
