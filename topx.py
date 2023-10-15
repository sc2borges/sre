import heapq
import argparse

def topX(filename, X):
    min_heap = []

    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            if len(min_heap) < X:
                heapq.heappush(min_heap, number)
            else:
                if number > min_heap[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, number)

    largest_numbers = sorted(min_heap, reverse=True)
    return largest_numbers

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find the top X largest numbers in a file.')
    parser.add_argument('filename', type=str, help='Path to the file containing numbers')
    parser.add_argument('X', type=int, help='Number of largest numbers to find')
    args = parser.parse_args()

    result = topX(args.filename, args.X)
    print(f"Top {args.X} largest numbers:", result)

