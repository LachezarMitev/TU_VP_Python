av_pr = set(input().split())
rec_name = input()
rec_pr = set(input().split())

pr_diff = len(rec_pr) - len(av_pr)

print(f"There are {len(rec_pr)} products for {rec_name}: {rec_pr}")
if(pr_diff > 0):
    print(f"You need to buy {pr_diff} products: {rec_pr - av_pr}")
else: print(f"Unnecessary products: {av_pr - rec_pr}")