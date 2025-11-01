modal = 100000000
laba = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03]

profit = [rate * modal for rate in laba]

for i, profit in enumerate(profit, start=1):
    print("laba bulan ke-", i, "sebesar:", profit)



