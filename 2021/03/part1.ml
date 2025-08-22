open Stdio
open Base

let rec pow2 i = match i with
  | 0 -> 1
  | _ -> 2 * pow2 (i-1)

let filename = "data.txt"
let data = In_channel.input_all @@ In_channel.create filename

let nums = String.split data ~on:'\n'
let n = String.length @@ List.hd_exn nums

let rec count l vals = match l with
  | [] -> List.rev @@ List.map vals ~f:(fun x -> if x < 0 then 0 else 1) 
  | s :: t -> count t (List.map2_exn (List.init n ~f:(fun i -> if Char.equal '1' s.[i] then 1 else -1)) vals ~f:(+))

let gamma = count nums @@ List.init n ~f:(fun _ -> 0)
let delta = List.map gamma ~f:(fun i -> 1-i)

let rate (l : int list) = Base.List.foldi l ~init:0 ~f:(fun i y x -> y + x * (pow2 i))

let () = Stdio.print_endline @@ Int.to_string @@ (rate gamma) * (rate delta)
