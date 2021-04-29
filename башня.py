def move_tower(height,from_peg, to_peg, with_peg):
    if height >= 1:
        move_tower(height-1,from_peg,with_peg,to_peg)
        move_disk(from_peg,to_peg)
        move_tower(height-1,with_peg,to_peg,from_peg)

def move_disk(fp,tp):
    print("moving from",fp,"to",tp)

move_tower(3,"A","B","C")
