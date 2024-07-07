"""
CCC '24 J1 - 'Conveyor Belt Sushi'
Problem link: https://dmoj.ca/problem/ccc24j1
Score received : 15/15
"""

def main():
  r = int(input()) # take in input of how many red, green, and blue plates
  g = int(input())
  b = int(input())

  print(r*3 + g*4 + b*5) # multiply number of plates by their respective costs

main()
