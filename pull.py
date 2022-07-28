import pandas as pd  

df = pd.read_csv("atp.csv")
def pull_data(player, opp_rank):

    df = pd.read_csv("atp.csv")
    df_chall = pd.read_csv("atp_chall.csv")
    df = df.append(df_chall)
    df2 = pd.read_csv("atp_2.csv")
    df_chall_2 = pd.read_csv("atp_2_chall.csv")
    df = df.append(df_chall_2)
    df = df.append(df2)
    # df3 = pd.read_csv("atp_3.csv")
    # df = df.append(df3)
    # df4 = pd.read_csv("atp_4.csv")
    # df = df.append(df4)
    def conv(x):
        try:
            if(int(x)) <= opp_rank:
                return True
            else:
                return False
        except:
            return False
    



    winnings = df.loc[(df['winner_name'] == f"{player}")  & (df['loser_rank'].apply(lambda x: conv(x)) == True) & (df["surface"] == "Clay") & (df["tourney_level"].str.contains("A|M|F|G"))]
    losings = df.loc[(df['loser_name'] == f"{player}")  & (df['winner_rank'].apply(lambda x: conv(x)) == True) & (df["surface"] == "Clay") & (df["tourney_level"].str.contains("A|M|F|G"))]


    ace_rate  = (winnings["w_ace"].sum() + losings["l_ace"].sum())/(winnings["w_svpt"].sum() + losings["l_svpt"].sum())
    
    df_rate = (winnings["w_df"].sum() + losings["l_df"].sum())/(winnings["w_svpt"].sum() + losings["l_svpt"].sum())

    serve_rate = (winnings["w_1stIn"].sum() + losings["l_1stIn"].sum())/(winnings["w_svpt"].sum() + losings["l_svpt"].sum())

    first_serve_points_win_rate = (winnings["w_1stWon"].sum() + losings["l_1stWon"].sum())/(winnings["w_1stIn"].sum() + losings["l_1stIn"].sum())
    second_serve_points_win_rate = (winnings["w_2ndWon"].sum() + losings["l_2ndWon"].sum())/((winnings["w_svpt"].sum() + losings["l_svpt"].sum())-(winnings["w_1stIn"].sum() + losings["l_1stIn"].sum()))

    first_serve_return_points_win_rate = ((winnings["l_1stIn"].sum())-(winnings["l_1stWon"].sum())+ (losings["w_1stIn"].sum())-(losings["w_1stWon"].sum()))/((winnings["l_1stIn"].sum()) + (losings["w_1stIn"].sum()))

    second_serve_return_points_win_rate = ((winnings["l_svpt"].sum())-(winnings["l_1stIn"].sum())+ (losings["w_svpt"].sum())-(losings["w_1stIn"].sum())-((winnings["l_2ndWon"].sum()) + (losings["w_2ndWon"].sum())))/((winnings["l_svpt"].sum())-(winnings["l_1stIn"].sum())+ (losings["w_svpt"].sum())-(losings["w_1stIn"].sum()))

    bp_conversion = (((winnings["l_bpFaced"].sum())+(losings["w_bpFaced"].sum()))-((winnings["l_bpSaved"].sum())+(losings["w_bpSaved"].sum())))/(winnings["l_bpFaced"].sum()+losings["w_bpFaced"].sum())

    returnace = (losings["w_ace"].sum() + winnings["l_ace"].sum())/(winnings['l_svpt'].sum()+losings['w_svpt'].sum())

    bp_saved = (winnings["w_bpSaved"].sum()+losings["l_bpSaved"].sum())/(winnings["w_bpFaced"].sum()+losings["l_bpFaced"].sum())

    val = {
        
        "name": player,
        "ace" : ace_rate,
        "df" : df_rate,
        "1stin" : serve_rate,
        "1st%" : first_serve_points_win_rate,
        "2nd%" : second_serve_points_win_rate,
        "1streturn" : first_serve_return_points_win_rate,
        "2ndreturn" : second_serve_return_points_win_rate,
        "returnace": returnace,
        "bp": bp_conversion,
        "bp_saved": bp_saved
        


    }
    # three = df["score"]
    # coutner = 0
    # y = 0
    # for x in three:
    #     y += 1
    #     x = str(x)
    #     if x.count("-") == 3:
    #         coutner +=1 
    #     print(coutner)
    #     print(y)

    return val


# pull_data("Novak Djokovic", 60)