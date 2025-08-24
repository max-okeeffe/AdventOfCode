open Stdio
open Base

let filename = "data.txt"
let data = In_channel.input_all @@ In_channel.create filename

let format s = s
  |> String.split_on_chars ~on:[' '; '-'; '>']
  |> List.filter ~f:(fun x -> not @@ String.equal x "")
  |> List.map ~f:(fun s -> s |> String.split ~on: ',' |> List.map ~f:Int.of_string)

let ends = List.filter ~f:(fun x -> match x with [[a;b];[c;d]] -> a=c || b=d | _ ->  false) @@ List.map ~f:format @@ String.split_lines data

let overlap h z =
  match h, z with
  | [[a;b];[c;d]], [x;y] -> x = a && min b d <= y && y <= max b d || y = b && min a c <= x && x <= max a c
  | _ -> false

let expand l =
  match l with
  | [[a;b];[c;d]] when a = c -> List.init (abs (d-b) + 1) ~f:(fun i -> [a; i + min b d])
  | [[a;b];[c;d]] when b = d -> List.init (abs (c-a) + 1) ~f:(fun i -> [i + min a c; b])
  | _ -> [[]]

let get_list =
  let rec aux l f (curr : int list list) =
    match l with
    | h :: t ->
      let expand_h = expand h in
      let g = fun z -> f z + if overlap h z then 1 else 0 in
      aux t g ( (expand_h |> List.filter ~f:(fun x -> not @@ List.mem curr x ~equal:(List.equal (=)) && g x > 1 ) ) @ curr)
    | _ -> curr in
  List.length @@ aux ends (fun _ -> 0) []

let () = Stdio.print_endline @@ Int.to_string get_list
