if __name__ == "__main__":
    paper_total = 0
    ribbon_total = 0

    with open("input.txt") as f:
        for line in f:
            h, w, l = [int(x) for x in line.strip().split('x', 2)]

            paper_total += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

            ribbon_total += min(2*(h+w), 2*(w+l), 2*(h+l)) + h*w*l
    print(f'Part One: {paper_total}')
    print(f'Part Two: {ribbon_total}')