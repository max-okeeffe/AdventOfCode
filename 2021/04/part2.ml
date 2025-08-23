open Stdio
open Base

let filename = "data.txt"
let data = In_channel.input_all @@ In_channel.create filename

let split_list l =
  let rec aux out curr l =
    match l with
    | [] -> out
    | "" :: t -> aux (out @ [curr]) [] t
    | x :: t -> aux out (curr @ [x]) t in
  aux [] [] l

let bingo = split_list @@ String.split data ~on:'\n'
let nums = List.map (String.split (List.hd_exn @@ List.hd_exn bingo) ~on:',') ~f:Int.of_string

let make_board board =
  let rec aux board curr =
    match board with
    | [] -> curr
    | h::t -> 
      [| Array.map ( Array.of_list @@ List.filter (String.split h ~on:' ') ~f:(fun x -> not @@ String.equal x "")) ~f:Int.of_string |]
      |> Array.append curr
      |> aux t in
  aux board [||]
  
let boards = List.map (List.tl_exn bingo) ~f:make_board

let play n boards = 
  let aux board = Array.map board ~f:( fun row -> Array.map row ~f:(fun i -> if i = n then -1 else i) ) in
  List.map boards ~f:aux

let wins board =
  let winning_row board = Array.exists board ~f:(fun row -> Array.fold row ~init:0 ~f:(+) = -5) in
  winning_row board || winning_row @@ Array.transpose_exn board

let score board =
  let aux row = Array.fold (Array.filter row ~f:(fun i -> i <> -1)) ~init:0 ~f:(+) in
  aux @@ Array.map board ~f:aux

let rec game nums boards = 
  match nums with
  | [] -> 0
  | h::t ->
    let play_h = play h boards in let get_winning = List.filter ~f:wins play_h in
    match get_winning, boards with
    | [], _ -> game t play_h
    | _, [] -> 0
    | [x], [_] -> (score x) * h
    | _ -> game t (List.filter play_h ~f:(fun x -> not @@ wins x))

let () = Stdio.print_endline @@ Int.to_string @@ game nums boards
