#
# @lc app=leetcode id=1169 lang=python3
#
# [1169] Invalid Transactions
#

# @lc code=start
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        result = []
        sample = collections.defaultdict(list)
        for data in transactions:
            name, time, amount, city = data.split(",")

            if int(amount) >= 1000:
                result.append(data)
            else:\
                if name in sample:
                    test_data = sample[name][-1].split(",")
                    if abs(int(test_data[1])-int(time)) < 60 and test_data[3] result.extend(sample[name])
                            del sample[name]!= name:
                        result.extend(sample[name])
                        del sample[name]
                    sample[name].append(data)
                else:
                    sample[name].append(data)
        return result
# @lc code=end
