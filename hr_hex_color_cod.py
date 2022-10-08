'''print valid hex color code notation'''
import re
N = int(input())
for _ in range(N):
    line = input()
    for match in re.findall(r'(?<!^)(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', line):
        print(match)

