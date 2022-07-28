import random
import os
from pull import pull_data
POINTS = ('0', '15', '30', '40')

p1 = pull_data("Stefanos Tsitsipas", 10)

p2 = pull_data("Casper Ruud", 10)

p1['1st%'] = ((p1["1st%"])+(1-p2["1streturn"]))/2
p1['2nd%'] = ((p1["2nd%"])+(1-p2["2ndreturn"]))/2
p2['1st%'] = ((p2["1st%"])+(1-p1["1streturn"]))/2
p2['2nd%'] = ((p2["2nd%"])+(1-p1["2ndreturn"]))/2
p1["ace"] =  ((p1["ace"])+(p2["returnace"]))/2
p2["ace"] =  ((p2["ace"])+(p1["returnace"]))/2
p1["bp"] = ((1-p2["bp_saved"])+p1["bp"])/2
p2["bp"] = ((1-p1["bp_saved"])+p2["bp"])/2


  
def reset_game():
  global p1_game_count,p2_game_count
  p1_game_count = 0
  p2_game_count = 0


p1_set_count = 0
p2_set_count = 0

p1_ace_count = 0
p2_ace_count = 0

p1_df_count = 0
p2_df_count = 0

points_count = 0
score = []

p1_bp_count = 0
p2_bp_count = 0
p1_bp_saved = 0
p2_bp_saved = 0

p1_match_count = 0
p2_match_count = 0

p1_servepts = 0
p2_servepts = 0
p1_servesin = 0
p2_servesin = 0


def increment_point(player_points, scorer):
  
	if player_points == ['40', '40']:
		scorer_points = 'ADV'
	else:
		try:
			scorer_points = POINTS[POINTS.index(player_points[scorer]) + 1]
		except IndexError:
			scorer_points = 'WIN'
	return scorer_points


def point_scored(score, scorer):
  scorer -= 1
  global points_count
  points_count +=1
  loser = abs(1 - scorer)
  player_points = score.split()
  if player_points[loser] == 'ADV':
	  player_points[loser] = '40'
  elif player_points[scorer] == 'ADV':
    player_points[scorer] = 'WIN'
  else:
    player_points[scorer] = increment_point(player_points, scorer)
  return ' '.join(player_points)


def ran():
  return random.uniform(0,1)



def p1_who_wins_point():
  global p1_servepts
  p1_servepts +=1
  if ran() <(p1["ace"]):
    # print("Ace")
    global p1_ace_count
    p1_ace_count += 1
    global p1_servesin
    p1_servesin+=1
    return 1
  if ran() < p1["df"]:
    global p1_df_count
    p1_df_count +=1
    # print("DF")
    return 2
  if ran() < p1["1stin"]: 
    p1_servesin+=1
    if ran() < (p1["1st%"]):
      # print("First serve point won.")
      return 1
    else:
      # print("First serve point lost.")
      return 2

  elif ran() < (p1["2nd%"]):
    # print("Second serve point won.")
    return 1
  else:
    # print("Second serve point lost.")
    return 2


def p2_who_wins_point():
  global p2_servepts
  p2_servepts +=1
  if ran() <(p2["ace"]):
    # print("Ace")
    global p2_ace_count
    p2_ace_count += 1
    global p2_servesin
    p2_servesin+=1
    return 2
  if ran() < p2["df"]:
    global p2_df_count
    p2_df_count +=1
    # print("DF")
    return 1
  if ran() < p2["1stin"]:
    p2_servesin+=1 
    if ran() < (p2["1st%"]):
      # print("First serve point won.")
      return 2
    else:
      # print("First serve point lost.")
      return 1
  
  elif ran() < (p2["2nd%"]):
    # print("Second serve point won.")
    return 2
  else:
    # print("Second serve point lost.")
    return 1



def p1_service_game():
  print(f"{p1['name']} Serving")
  current_score = '0 0'
  while True:
    
    if "WIN" in current_score:
      if current_score.startswith(tuple('WIN')):
        # print("Servers game.")
        global p1_game_count
        p1_game_count += 1
        break
      else:
        # print("Break")
        global p2_game_count
        p2_game_count +=1
        break
    if (current_score.endswith("40") and (current_score.startswith("30") or current_score.startswith("15") or current_score.startswith("0"))) or current_score.endswith("ADV") and current_score.startswith("40"):
      if current_score != "40 40":
        global p2_bp_count
        p2_bp_count += 1
        if ran() < p2["bp"]:
  
          print("Break")
          current_score = point_scored(current_score, 2)
          print(current_score)
          p2_game_count +=1
          break
        else:
          # print(current_score)
          print("Break Saved")
          global p1_bp_saved
          p1_bp_saved += 1
          current_score = point_scored(current_score, 1)
          print(current_score)
          continue
    current_score = point_scored(current_score, p1_who_wins_point())
    print(current_score)

  return f"{p1_game_count}-{p2_game_count}"


def p2_service_game():
  print(f"{p2['name']} Serving")
  current_score = '0 0'
  while True:
    
    if "WIN" in current_score:
      if current_score.startswith(tuple('WIN')):
        # print("Break")
        global p1_game_count
        p1_game_count += 1
        break
      else:
        # print("Servers game.")
        global p2_game_count
        p2_game_count +=1
        break
    if (current_score.startswith("40") and (current_score.endswith("30") or current_score.endswith("15") or current_score.endswith("0"))) or (current_score.startswith("ADV") and current_score.endswith("40")):
      if current_score != "40 40":
        global p1_bp_count
        p1_bp_count +=1
        if ran() < p1["bp"]:
          
          print("Break")
          current_score = point_scored(current_score, 1)
          print(current_score)
          p1_game_count +=1
          break
        else:
          # print(current_score)
          print("Break Point Saved")
          global p2_bp_saved
          p2_bp_saved +=1
          current_score = point_scored(current_score, 2)
          print(current_score)
          continue
    current_score = point_scored(current_score, p2_who_wins_point())
    print(current_score)

  return f"{p1_game_count}-{p2_game_count}"

def get_game_count():
  return f"{p1_game_count}-{p2_game_count}"

def tiebreak_p1():
  p1_score = 0
  p2_score = 0
  res = p1_who_wins_point()
  if res == 1:
    p1_score += 1
  else:
    p2_score+=1
  while True:
    if p1_score >= 7 and p2_score <= (p1_score-2) or p2_score >= 7 and p1_score <= (p2_score-2):
      # print(p1_score, p2_score)
      if p1_score > p2_score:
        global p1_game_count
        p1_game_count += 1
        return 1

      else:
        global p2_game_count
        p2_game_count +=1
        return 2

    res = p2_who_wins_point()
          
    if res == 2:
      p2_score += 1
    else:
      p1_score+=1
    if p1_score >= 7 and p2_score <= (p1_score-2) or p2_score >= 7 and p1_score <= (p2_score-2):
      # print(p1_score, p2_score)
      if p1_score > p2_score:

        p1_game_count += 1
        return 1
      else:

        p2_game_count +=1
        return 2

    res = p2_who_wins_point()
          
    if res == 2:
      p2_score += 1
    else:
      p1_score+=1
    if p1_score >= 7 and p2_score <= (p1_score-2) or p2_score >= 7 and p1_score <= (p2_score-2):
      # print(p1_score, p2_score)
      if p1_score > p2_score:

        p1_game_count += 1
        return 1
      else:

        p2_game_count +=1
        return 2

    res = p1_who_wins_point()
    if res == 1:
      p1_score += 1
    else:
      p2_score+=1
    if p1_score >= 7 and p2_score <= (p1_score-2) or p2_score >= 7 and p1_score <= (p2_score-2):
      # print(p1_score, p2_score)
      if p1_score > p2_score:

        p1_game_count += 1
        return 1
      else:

        p2_game_count +=1
        return 2

    res = p1_who_wins_point()
    if res == 1:
      p1_score += 1
    else:
      p2_score+=1






def tiebreak_p2():
  p1_score = 0
  p2_score = 0
  res = p2_who_wins_point()
  if res == 1:
    p1_score += 1
  else:
    p2_score+=1
  while True:
    if p1_score >= 7 and p2_score <= (p1_score-2) or p2_score >= 7 and p1_score <= (p2_score-2):
      if p1_score > p2_score:
        global p1_game_count
        p1_game_count += 1
        return 1
      else:
        global p2_game_count
        p2_game_count +=1
        return 2

    res = p1_who_wins_point()
          
    if res == 2:
      p2_score += 1
    else:
      p1_score+=1
    if p1_score >= 7 and p2_score <= (p1_score-2) or p2_score >= 7 and p1_score <= (p2_score-2):
      # print(p1_score, p2_score)
      if p1_score > p2_score:

        p1_game_count += 1
        return 1
      else:

        p2_game_count +=1
        return 2

    res = p1_who_wins_point()
          
    if res == 2:
      p2_score += 1
    else:
      p1_score+=1
    if p1_score >= 7 and p2_score <= (p1_score-2) or p2_score >= 7 and p1_score <= (p2_score-2):
      # print(p1_score, p2_score)
      if p1_score > p2_score:

        p1_game_count += 1
        return 1
      else:

        p2_game_count +=1
        return 2

    res = p2_who_wins_point()
    if res == 1:
      p1_score += 1
    else:
      p2_score+=1
    if p1_score >= 7 and p2_score <= (p1_score-2) or p2_score >= 7 and p1_score <= (p2_score-2):
      # print(p1_score, p2_score)
      if p1_score > p2_score:

        p1_game_count += 1
        return 1
      else:

        p2_game_count +=1
        return 2

    res = p2_who_wins_point()
    if res == 1:
      p1_score += 1
    else:
      p2_score+=1

def handicap_p1():
  
  p1['1st%'] += 0.04
  p1['2nd%'] += 0.04
  
def handicap_p2():
 
  p2['1st%'] += 0.04
  p2['2nd%'] += 0.04
  
  


def set_check(res, server):
    if '6' in res and (int(res[-1]) < 5 or int(res[0]) < 5): 
      if res.startswith('6'):
        set_score = get_game_count()
        score.append(set_score)
        print(f"Set {p1['name']}")
        global p1_set_count
        p1_set_count +=1
        handicap_p1()
        return True
      elif res.endswith('6'):
        set_score = get_game_count()
        score.append(set_score)
        print(f"Set {p2['name']}")
        global p2_set_count
        p2_set_count +=1
        handicap_p2()
        return True
    elif res[0] == '6' and res[-1] == '6':
      
      if server == 1:
        print(f"Tiebreak {p2['name']} serving first")
        res = tiebreak_p2()
        if res == 1:
          set_score = get_game_count()
          score.append(set_score)
          print(get_game_count())
          print(f"Set {p1['name']}")
          
          p1_set_count +=1
          handicap_p1()
          return True
        else:
          set_score = get_game_count()
          score.append(set_score)
          print(get_game_count())
          print(f"Set {p2['name']}")
          
          p2_set_count +=1 
          handicap_p2()
        
          return True
      else:
        print(f"Tiebreak {p1['name']} serving first")
        res = tiebreak_p1()
        if res == 1:
          set_score = get_game_count()
          score.append(set_score)
          print(f"Set {p1['name']}")
          print(get_game_count())
          p1_set_count +=1
          handicap_p1()
          return True
        else:
          set_score = get_game_count()
          score.append(set_score)
          
          print(f"Set {p2['name']}")
          print(get_game_count())
          p2_set_count +=1
          handicap_p2() 
        
          return True
          
          

    elif '7' in res and int(res[-1]) == 5:
      set_score = get_game_count()
      score.append(set_score)
      print(f"Set {p1['name']}")
      

      p1_set_count +=1
      handicap_p1()
      return True
    elif '5' in res and int(res[-1]) == 7:
      set_score = get_game_count()
      score.append(set_score)
      print(f"Set {p2['name']}")
      

      p2_set_count +=1
      handicap_p2()
      return True


def set(server):
  reset_game()
  res = "0"
  if server == 1:
    print(get_game_count())
    for x in range(12):
      
      check=set_check(res, 2)
      if check:
        return 1
        break
      res = p1_service_game()
      print(get_game_count())
      check = set_check(res, 1)
      if check:
        return 2
        break
      res = p2_service_game()
      print(get_game_count())
  if server == 2:
  
    for x in range(12):
      
      check=set_check(res, 1)
      if check:
        return 2
        break
      res = p2_service_game()
      print(get_game_count())
      check = set_check(res, 2)
      if check:
        return 1
        break
      res = p1_service_game()
      print(get_game_count())
  

threeset = 0


for x in range(1000):


  p1_set_count = 0
  p2_set_count = 0

  p1_ace_count = 0
  p2_ace_count = 0

  p1_df_count = 0
  p2_df_count = 0

  points_count = 0
  score = []

  p1_bp_count = 0
  p2_bp_count = 0
  p1_bp_saved = 0
  p2_bp_saved = 0
    
  jambon = 1
  jambon = set(jambon)

  jambon = set(jambon)
  if p1_set_count == p2_set_count:

  
    threeset+=1
    set(jambon)
  
  def clear():
      os.system('clear')
  
  
  if p1_set_count > p2_set_count:
    
    print(f"Match {p1['name']}: {' '.join(score)}")
    print(f"{p1['name']} Break Points: {p1_bp_count-p2_bp_saved}/{p1_bp_count}")
    print(f"{p2['name']} Break Points: {p2_bp_count-p1_bp_saved}/{p2_bp_count}")
    print(f"{p1['name']} Aces: {p1_ace_count}")
    print(f"{p2['name']} Aces: {p2_ace_count}")
    print(f"{p1['name']} DF: {p1_df_count}")
    print(f"{p2['name']} DF: {p2_df_count}")
    print(f"{p1['name']} First Serve %: {p1_servesin/p1_servepts}")
    print(f"{p2['name']} First Serve %: {p2_servesin/p2_servepts}")
    p1['1st%'] -= p1_set_count * 0.04
    p1['2nd%'] -= p1_set_count * 0.04
    p2['1st%'] -= p2_set_count * 0.04
    p2['2nd%'] -= p2_set_count * 0.04
    p1_match_count += 1
    print(f"There was {points_count} points in the match.")
    print(f"{p1['name']} has a", p1_match_count/(p2_match_count+p1_match_count), "chance of winning.")

    print(f"{p2['name']} has a", p2_match_count/(p2_match_count+p1_match_count), "chance of winning.")
    print(f"There was {threeset} three set matches out of 1000")
    
  else:
  
    print(f"Match {p2['name']}: {' '.join(score)}")
    print(f"{p1['name']} Break Points Converted: {p1_bp_count-p2_bp_saved}/{p1_bp_count}")
    print(f"{p2['name']} Break Points Converted: {p2_bp_count-p1_bp_saved}/{p2_bp_count}")
    print(f"{p1['name']} Aces: {p1_ace_count}")
    print(f"{p2['name']} Aces: {p2_ace_count}")
    print(f"{p1['name']} DFs: {p1_df_count}")
    print(f"{p2['name']} DFs: {p2_df_count}")
    print(f"{p1['name']} First Serve %: {p1_servesin/p1_servepts}")
    print(f"{p2['name']} First Serve %: {p2_servesin/p2_servepts}")
    p1['1st%'] -= p1_set_count * 0.04
    p1['2nd%'] -= p1_set_count * 0.04
    p2['1st%'] -= p2_set_count * 0.04
    p2['2nd%'] -= p2_set_count * 0.04
    p2_match_count +=1
    print(f"There was {points_count} points in the match.")

    print(f"{p1['name']} has a", p1_match_count/(p2_match_count+p1_match_count), "chance of winning.")

    print(f"{p2['name']} has a", p2_match_count/(p2_match_count+p1_match_count), "chance of winning.")
  
    print(f"There was {threeset} three set matches out of 1000")
  