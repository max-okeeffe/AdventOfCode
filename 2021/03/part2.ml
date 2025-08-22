open Stdio
open Base

let rec pow2 i = match i with
  | 0 -> 1
  | _ -> 2 * pow2 (i-1)

let filename = "data.txt"
let data = In_channel.input_all @@ In_channel.create filename

let nums = String.split data ~on:'\n'
let n = String.length @@ List.hd_exn nums

let count arr i most =
  let temp = List.fold arr ~init:0 ~f:(fun y x -> y + (if Char.equal '1' x.[i] then 1 else -1)) in
  match most with
  | true -> if temp < 0 then '0' else if temp > 0 then '1' else 'e'
  | false -> if temp < 0 then '1' else if temp > 0 then '0' else 'e'

let rec bit l i most = match l with
  | [] -> []
  | [x] -> List.rev @@ List.init n ~f:(fun i -> if Char.equal x.[i] '1' then 1 else 0)
  | _ -> let b = count l i most in
        let def = if most then '1' else '0' in
        let k = if Char.equal b 'e' then def else b in
        bit (List.filter l ~f:(fun s -> Char.equal s.[i] k)) (Int.rem (i+1) n) most

let oxygen = bit nums 0 true
let co2 = bit nums 0 false

let rate (l : int list) = Base.List.foldi l ~init:0 ~f:(fun i y x -> y + x * (pow2 i))

let () = Stdio.print_endline @@ Int.to_string @@ (rate oxygen) * (rate co2)
