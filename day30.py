print("30 days down")
for i in range(1,31):
  print(f"What is your thought for Day {i}:")
  thought = input()
  print()
  response = f"""You thought Day {i} was 
  {thought:^10}"""
  print(response)
  print()
  