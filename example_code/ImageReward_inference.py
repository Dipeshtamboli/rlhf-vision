# pip3 install image-reward
# pip3 install clip

import ImageReward as RM
model = RM.load("ImageReward-v1.0")
prompts = ["code screenshot", "python", "python snake", "python code"]
img_paths = ["code.png"]
for prompt in prompts:
	reward = model.score(prompt, img_paths)
	print(f"{prompt}: {reward}")


# Output:
# code screenshot: 0.9415892362594604
# python: -0.4653015434741974
# python snake: -1.3486034870147705
# python code: 0.5567578673362732
