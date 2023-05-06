series = 0
max_series = 0
previous = 0
max = 0

print("Please enter the lengths of the jumps: ")
a = float(input())

while a != 0:
  if a > max:
    max = a
  if a > previous:
    previous = a
    series = series + 1
  else:
    previous = a
    if max_series < series:
      max_series = series
    series = 1
  a = float(input())

if max_series < series:
  max_series = series

print("\The longest jump:", max, "m")
print("\nThe longest series of jumps: ", max_series)
