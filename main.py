import random
#Creating player's profile
Player=input("what is the name of your player?")
Position=input("what is the player's position?")
Team=input("What team does he play for?")
Conference=input("which conference will he represent?")
A=random.randint(0,2)

#determining the quality of the player's season
a=0
#good season
if A ==0:
  print(f"{Player} had a great season! Here are his stats:")
  Pts=random.randint(25,40)
  Stl=random.randint(1,5)
  Blk=random.randint(2,5)
  Rbd=random.randint(4,9)
  Ast=random.randint(6,12)
  FanVote=random.randint(6000000,7500000)
  PlayerVote=random.randint(140,220)
  MediaVote=random.randint(65,100)

  #average season
elif A==1:
  print(f"{Player} had an average season. Here are his stats:")
  Pts=random.randint(15,24)
  Stl=random.randint(0,3)
  Blk=random.randint(0,3)
  Rbd=random.randint(2,6)
  Ast=random.randint(3,6)
  FanVote=random.randint(2200000,6550000)
  PlayerVote=random.randint(100,170)
  MediaVote=random.randint(43,75)

  #poor seson
else:
  print(f"{Player} had a poor season. Here are his stats:")
  a==1.3
  Pts=random.randint(5,14)
  Stl=random.randint(0,2)
  Blk=random.randint(0,3)
  Rbd=random.randint(0,4)
  Ast=random.randint(1,4)
  FanVote=random.randint(0,55000)
  PlayerVote=random.randint(3,12)
  MediaVote=random.randint(0,8)
  
#building his final stats
stats ={
  'Pts':Pts,
  'Ast':Ast,
  'Rbd':Rbd,
  'Blk':Blk,
  'Stl':Stl
}
print(stats)

#creating his fan,media,and player votes to make a weighted score


#Ranking based off fan votes
if FanVote >= 6500000:
  FanRank=random.randint(1,4)
elif FanVote >= 2450000 and FanVote <=6499999:
  FanRank=random.randint(6,15)
else:
  FanRank=random.randint(16,25)

#Ranking based off player votes
if PlayerVote >= 160:
  PlayerRank=random.randint(1,4)
elif PlayerVote >= 89 and PlayerVote <=159:
  PlayerRank=random.randint(6,15)
else:
  PlayerRank=random.randint(16,25)
  
#Ranking based off Media votes
if MediaVote >= 72:
  MediaRank=random.randint(1,4)
elif MediaVote >= 19 and MediaVote <=45:
  MediaRank=random.randint(5,7)
else:
  MediaRank=random.randint(8,9)
AScore=((FanRank*2)+PlayerRank+MediaRank)/4



  
#revealing the player's final rankings!
print(f"Now, we have the {Team}'s {Position}:{Player}! His Fan Vote was {FanVote}, he ended up ranking {FanRank} in that field. For player votes, he got {PlayerVote}, he ranked {PlayerRank} in that field. Lastly, he got {MediaVote} votes from the media, and he ranked {MediaRank} in that field. His final all-star ranking was {AScore}")

#Deciding whether your player was good enough to make the all-star team for his conference!
if AScore <= 4 and A<=1:
  print(f"{Player} has made it into this year's all-star game! He will be the {Position} for the {Conference} Conference!")
else:
  print(f"unfortunately, {Player} did not make it into the {Conference}'s all-star team this year.")


