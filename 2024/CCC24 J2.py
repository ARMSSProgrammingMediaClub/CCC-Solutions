"""
CCC '24 J2 - 'Dusa and The Yobis"
Problem Link: https://dmoj.ca/problem/ccc24j2
Score received: 15/15
"""
def main():
  dusa = int(input()) # take in first line which is the initial Dusa size
  for _ in range(100000000): 
    yobis = int(input()) # take yobi size value. Put inside forloop as it checks multiple lines of yobi
    if dusa <= yobis: # if the dusa is smaller or equal to the yobi size. Then breaks the forloop and prints current dusa size
      print(dusa)
      break
    else:
      dusa += yobis # if dusa is larger than yobi, then add the yobi size to the dusa then repeat for next line

main()
