def main():
  dusa = int(input())
  for _ in range(100000000):
    yobis = int(input())
    if dusa <= yobis:
      print(dusa)
      break
    else:
      dusa += yobis

main()