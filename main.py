
def count_batteries_by_health(present_capacities):
  counts = {           
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
  for i in present_capacities:
    rated_capacity=120 
    soh=(i/rated_capacity)*100   
   
    if soh>100:
      soh=100 
    if soh>=80:
      counts["healthy"]+=1
      print(f"Battery with SoH {soh}% and present capacity {i} Ah is classified as 'healthy'.")
    elif 63<=soh<80:
      counts["exchange"]+=1
      print(f"Battery with SoH {soh}% and present capacity {i} Ah is classified as 'exchange'.")
    else:
      counts["failed"]+=1
      print(f"Battery with SoH {soh}% and present capacity {i} Ah is classified as 'failed'.")
  return counts


def test_bucketing_by_health():  
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 72]
  counts = count_batteries_by_health(present_capacities)
  assert counts["healthy"] == 2
  assert counts["exchange"] == 3
  assert counts["failed"] == 1
  print(counts)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
