volume_cols = [
    # Finishing
    "goals",
    "expectedgoals",
    "goals_minus_xg",
    "totalshots",
    "shotsontarget",
    "shotsofftarget",
    "shotsfrominsidethebox",
    "shotsfromoutsidethebox",
    "hitwoodwork",
    "leftfootgoals",
    "rightfootgoals",
    "headedgoals",
    "goalsfrominsidethebox",
    "goalsfromoutsidethebox",
    "freekickgoal",
    "penaltiestaken",
    "penaltygoals",
    "bigchancesmissed",

    # Creativity
    "assists",
    "expectedassists",
    "assists_minus_xa",
    "goalsassistssum",
    "totalpasses",
    "accuratepasses",
    "inaccuratepasses",
    "totaloppositionhalfpasses",
    "accurateoppositionhalfpasses",
    "totalownhalfpasses",
    "accurateownhalfpasses",
    "accuratefinalthirdpasses",
    "keypasses",
    "totalattemptassist",
    "passtoassist",
    "bigchancescreated",
    "totallongballs",
    "accuratelongballs",
    "totalchippedpasses",
    "accuratechippedpasses",
    "totalcross",
    "accuratecrosses",

    # Possession
    "touches",
    "possessionlost",
    "dispossessed",
    "totalcontest",
    "successfuldribbles",
    "offsides",
    "wasfouled",
    "fouls",

    # Defensive
    "tackles",
    "tackleswon",
    "interceptions",
    "ballrecovery",
    "possessionwonattthird",
    "clearances",
    "blockedshots",
    "dribbledpast",
    "errorleadtoshot",
    "errorleadtogoal",

    # Duels
    "totalduelswon",
    "duellost",
    "groundduelswon",
    "aerialduelswon",
    "aeriallost",
    
    # Goalkeeping
    "saves",
    "savescaught",
    "savesparried",
    "savedshotsfrominsidethebox",
    "savedshotsfromoutsidethebox",
    "goalsprevented",
    "runsout",
    "successfulrunsout",
    "goalkicks",
    "punches",
    "highclaims",
    "crossesnotclaimed",
    'cleansheet',
    'goalsconceded',
    'goalsconcededinsidethebox',
    'goalsconcededoutsidethebox',
    'penaltyfaced',
    'penaltysave',
    'penaltyconceded',
  
    

    # Discipline
    "yellowcards",
    "yellowredcards",
    "directredcards",
    'redcards',
    "owngoals",
    
    # Set-Pieces
    "attemptpenaltymiss",
    "attemptpenaltypost",
    "attemptpenaltytarget",
    "penaltywon",
    "setpiececonversion",
    "shotfromsetpiece"
]

rate_cols = [
    "goalconversionpercentage",
    "scoringfrequency",
    "goals_per_xg",
    "shots_on_target_pct",
    "inside_box_shot_pct",
    
    "assist_conversion",
    "xa_per_keypass",
    "final_third_pass_pct",
    "opp_half_pass_pct",
    "accuratepassespercentage",
    "accuratecrossespercentage",
    "accuratelongballspercentage",
    "successfuldribblespercentage",

    "dribbles_per_touch",
    "dispossessed_per_touch",
    "possession_lost_per_touch",

    "tackleswonpercentage",
    "defensive_actions",

    "totalduelswonpercentage",
    "groundduelswonpercentage",
    "aerialduelswonpercentage",

    "penaltyconversion",

    "rating",
    "totalrating",
    "countrating"
]

per90_cols = [

    "goals_per90",
    "expectedgoals_per90",
    "goals_minus_xg_per90",
    "totalshots_per90",
    "shotsontarget_per90",
    "shotsofftarget_per90",
    "shotsfrominsidethebox_per90",
    "shotsfromoutsidethebox_per90",
    "hitwoodwork_per90",
    "leftfootgoals_per90",
    "rightfootgoals_per90",
    "headedgoals_per90",
    "goalsfrominsidethebox_per90",
    "goalsfromoutsidethebox_per90",
    "freekickgoal_per90",
    "penaltiestaken_per90",
    "penaltygoals_per90",
    "bigchancesmissed_per90",

    "assists_per90",
    "expectedassists_per90",
    "assists_minus_xa_per90",
    "goalsassistssum_per90",
    "totalpasses_per90",
    "accuratepasses_per90",
    "inaccuratepasses_per90",
    "totaloppositionhalfpasses_per90",
    "accurateoppositionhalfpasses_per90",
    "totalownhalfpasses_per90",
    "accurateownhalfpasses_per90",
    "accuratefinalthirdpasses_per90",
    "keypasses_per90",
    "totalattemptassist_per90",
    "passtoassist_per90",
    "bigchancescreated_per90",
    "totallongballs_per90",
    "accuratelongballs_per90",
    "totalchippedpasses_per90",
    "accuratechippedpasses_per90",
    "totalcross_per90",
    "accuratecrosses_per90",

    "touches_per90",
    "possessionlost_per90",
    "dispossessed_per90",
    "totalcontest_per90",
    "successfuldribbles_per90",
    "offsides_per90",
    "wasfouled_per90",
    "fouls_per90",

    "tackles_per90",
    "tackleswon_per90",
    "interceptions_per90",
    "ballrecovery_per90",
    "possessionwonattthird_per90",
    "clearances_per90",
    "blockedshots_per90",
    'defensive_actions_per90',
    "dribbledpast_per90",
    "errorleadtoshot_per90",
    "errorleadtogoal_per90",

    "totalduelswon_per90",
    "duellost_per90",
    "groundduelswon_per90",
    "aerialduelswon_per90",
    "aeriallost_per90",

    "saves_per90",
    "savescaught_per90",
    "savesparried_per90",
    "savedshotsfrominsidethebox_per90",
    "savedshotsfromoutsidethebox_per90",
    "runsout_per90",
    "successfulrunsout_per90",
    "goalkicks_per90",
    "punches_per90",
    "highclaims_per90",
    "crossesnotclaimed_per90",

    "yellowcards_per90",
    "yellowredcards_per90",
    "directredcards_per90",
    "owngoals_per90"
]

per90_zscore_cols=[
    'goals_per90_zscore', 
    'expectedgoals_per90_zscore', 
    'goals_minus_xg_per90_zscore', 
    'totalshots_per90_zscore', 
    'shotsontarget_per90_zscore', 
    'shotsofftarget_per90_zscore', 
    'shotsfrominsidethebox_per90_zscore', 
    'shotsfromoutsidethebox_per90_zscore', 
    'hitwoodwork_per90_zscore', 
    'leftfootgoals_per90_zscore', 
    'rightfootgoals_per90_zscore', 
    'headedgoals_per90_zscore', 
    'goalsfrominsidethebox_per90_zscore', 
    'goalsfromoutsidethebox_per90_zscore', 
    'freekickgoal_per90_zscore', 
    'penaltiestaken_per90_zscore', 
    'penaltygoals_per90_zscore', 
    'bigchancesmissed_per90_zscore', 
    'assists_per90_zscore', 
    'expectedassists_per90_zscore', 
    'assists_minus_xa_per90_zscore', 
    'goalsassistssum_per90_zscore', 
    'totalpasses_per90_zscore', 
    'accuratepasses_per90_zscore', 
    'inaccuratepasses_per90_zscore', 
    'totaloppositionhalfpasses_per90_zscore', 
    'accurateoppositionhalfpasses_per90_zscore', 
    'totalownhalfpasses_per90_zscore', 
    'accurateownhalfpasses_per90_zscore', 
    'accuratefinalthirdpasses_per90_zscore', 
    'keypasses_per90_zscore', 
    'totalattemptassist_per90_zscore', 
    'passtoassist_per90_zscore', 
    'bigchancescreated_per90_zscore', 
    'totallongballs_per90_zscore', 
    'accuratelongballs_per90_zscore', 
    'totalchippedpasses_per90_zscore', 
    'accuratechippedpasses_per90_zscore', 
    'totalcross_per90_zscore', 
    'accuratecrosses_per90_zscore', 
    'touches_per90_zscore', 
    'possessionlost_per90_zscore', 
    'dispossessed_per90_zscore', 
    'totalcontest_per90_zscore', 
    'successfuldribbles_per90_zscore', 
    'offsides_per90_zscore', 
    'wasfouled_per90_zscore', 
    'fouls_per90_zscore', 
    'tackles_per90_zscore', 
    'tackleswon_per90_zscore', 
    'interceptions_per90_zscore', 
    'ballrecovery_per90_zscore', 
    'possessionwonattthird_per90_zscore', 
    'clearances_per90_zscore', 
    'blockedshots_per90_zscore', 
    'defensive_actions_per90_zscore',
    'dribbledpast_per90_zscore', 
    'errorleadtoshot_per90_zscore', 
    'errorleadtogoal_per90_zscore', 
    'totalduelswon_per90_zscore', 
    'duellost_per90_zscore', 
    'groundduelswon_per90_zscore', 
    'aerialduelswon_per90_zscore', 
    'aeriallost_per90_zscore', 
    'saves_per90_zscore', 
    'savescaught_per90_zscore', 
    'savesparried_per90_zscore', 
    'savedshotsfrominsidethebox_per90_zscore', 
    'savedshotsfromoutsidethebox_per90_zscore', 
    'runsout_per90_zscore', 
    'successfulrunsout_per90_zscore', 
    'goalkicks_per90_zscore', 
    'punches_per90_zscore', 
    'highclaims_per90_zscore', 
    'crossesnotclaimed_per90_zscore', 
    'yellowcards_per90_zscore', 
    'yellowredcards_per90_zscore', 
    'directredcards_per90_zscore', 
    'owngoals_per90_zscore'
    ]

metadata_features = [
    "player",
    "team",
    "player id",
    "team id",
    "league",
    "position",
]

general_features = [
    "appearances",
    "number_of_seasons",
    "matchesstarted",
    "minutesplayed",
    "rating",
]

availability_features = [
    "minutesplayed",
    "appearances",
    "matchesstarted",
    "number_of_seasons",
    "minutesplayed_zscore",
    "appearances_zscore",
    "matchesstarted_zscore",
]

volume_zscore_cols = [

    "goals_zscore",
    "expectedgoals_zscore",
    "goals_minus_xg_zscore",
    "totalshots_zscore",
    "shotsontarget_zscore",
    "shotsofftarget_zscore",
    "shotsfrominsidethebox_zscore",
    "shotsfromoutsidethebox_zscore",
    "hitwoodwork_zscore",
    "leftfootgoals_zscore",
    "rightfootgoals_zscore",
    "headedgoals_zscore",
    "goalsfrominsidethebox_zscore",
    "goalsfromoutsidethebox_zscore",
    "freekickgoal_zscore",
    "penaltiestaken_zscore",
    "penaltygoals_zscore",
    "bigchancesmissed_zscore",

    "assists_zscore",
    "expectedassists_zscore",
    "assists_minus_xa_zscore",
    "goalsassistssum_zscore",
    "totalpasses_zscore",
    "accuratepasses_zscore",
    "inaccuratepasses_zscore",
    "totaloppositionhalfpasses_zscore",
    "accurateoppositionhalfpasses_zscore",
    "totalownhalfpasses_zscore",
    "accurateownhalfpasses_zscore",
    "accuratefinalthirdpasses_zscore",
    "keypasses_zscore",
    "totalattemptassist_zscore",
    "passtoassist_zscore",
    "bigchancescreated_zscore",
    "totallongballs_zscore",
    "accuratelongballs_zscore",
    "totalchippedpasses_zscore",
    "accuratechippedpasses_zscore",
    "totalcross_zscore",
    "accuratecrosses_zscore",

    "touches_zscore",
    "possessionlost_zscore",
    "dispossessed_zscore",
    "totalcontest_zscore",
    "successfuldribbles_zscore",
    "offsides_zscore",
    "wasfouled_zscore",
    "fouls_zscore",

    "tackles_zscore",
    "tackleswon_zscore",
    "interceptions_zscore",
    "ballrecovery_zscore",
    "possessionwonattthird_zscore",
    "clearances_zscore",
    "blockedshots_zscore",
    "dribbledpast_zscore",
    "errorleadtoshot_zscore",
    "errorleadtogoal_zscore",

    "totalduelswon_zscore",
    "duellost_zscore",
    "groundduelswon_zscore",
    "aerialduelswon_zscore",
    "aeriallost_zscore",

    "saves_zscore",
    "savescaught_zscore",
    "savesparried_zscore",
    "savedshotsfrominsidethebox_zscore",
    "savedshotsfromoutsidethebox_zscore",
    "runsout_zscore",
    "successfulrunsout_zscore",
    "goalkicks_zscore",
    "punches_zscore",
    "highclaims_zscore",
    "crossesnotclaimed_zscore",

    "yellowcards_zscore",
    "yellowredcards_zscore",
    "directredcards_zscore",
    "owngoals_zscore",
    
    'attemptpenaltymiss_zscore',
    'attemptpenaltypost_zscore',
    'attemptpenaltytarget_zscore',
    'cleansheet_zscore',
    'goalsconceded_zscore',
    'goalsconcededinsidethebox_zscore',
    'goalsconcededoutsidethebox_zscore',
    'penaltyconceded_zscore',
    'penaltyfaced_zscore',
    'penaltysave_zscore',
    'penaltywon_zscore',
    'redcards_zscore',
    'setpiececonversion_zscore',
    'shotfromsetpiece_zscore',
    
]

rate_zscore_cols=[
    'goalconversionpercentage_zscore',
    'goals_per_xg_zscore',
    'shots_on_target_pct_zscore',
    'inside_box_shot_pct_zscore',
    'assist_conversion_zscore',
    'xa_per_keypass_zscore',
    'final_third_pass_pct_zscore',
    'opp_half_pass_pct_zscore',
    'dribbles_per_touch_zscore',
    'dispossessed_per_touch_zscore',
    'possession_lost_per_touch_zscore',
    'defensive_actions_zscore',
    'tackleswonpercentage_zscore',
    'totalduelswonpercentage_zscore',
    'groundduelswonpercentage_zscore',
    'aerialduelswonpercentage_zscore',
    'penaltyconversion_zscore',
    'successfuldribblespercentage_zscore',
    'accuratepassespercentage_zscore',
    'accuratelongballspercentage_zscore',
    'accuratecrossespercentage_zscore',
    'countrating_zscore',
    'rating_zscore',
    'scoringfrequency_zscore',
    'totalrating_zscore'
]


attacking_features = [
    # Efficiency / Percentages
    "goalconversionpercentage",
    "penaltyconversion",
    "setpiececonversion",
    "goals_per_xg",
    "shots_on_target_pct",
    "inside_box_shot_pct",
    "weak_foot_goals_pct",

    # Percentage z-scores
    "goalconversionpercentage_zscore",
    "penaltyconversion_zscore",
    "setpiececonversion_zscore",
    "goals_per_xg_zscore",
    "shots_on_target_pct_zscore",
    "inside_box_shot_pct_zscore",
    "weak_foot_goals_pct_zscore",

    # Per90 z-scores
    "goals_per90_zscore",
    "expectedgoals_per90_zscore",
    "goals_minus_xg_per90_zscore",
    "totalshots_per90_zscore",
    "shotsontarget_per90_zscore",
    "shotsofftarget_per90_zscore",
    "shotsfrominsidethebox_per90_zscore",
    "shotsfromoutsidethebox_per90_zscore",
    "hitwoodwork_per90_zscore",
    "leftfootgoals_per90_zscore",
    "rightfootgoals_per90_zscore",
    "headedgoals_per90_zscore",
    "goalsfrominsidethebox_per90_zscore",
    "goalsfromoutsidethebox_per90_zscore",
    "freekickgoal_per90_zscore",
    "penaltiestaken_per90_zscore",
    "penaltygoals_per90_zscore",
    "bigchancesmissed_per90_zscore",
]

creation_features = [
    # Raw percentages
    "accuratepassespercentage",
    "accuratelongballspercentage",
    "accuratecrossespercentage",

    "assist_conversion",
    "xa_per_keypass",
    "final_third_pass_pct",
    "opp_half_pass_pct",

    # Percentage z-scores
    "accuratepassespercentage_zscore",
    "accuratelongballspercentage_zscore",
    "accuratecrossespercentage_zscore",

    "assist_conversion_zscore",
    "xa_per_keypass_zscore",
    "final_third_pass_pct_zscore",
    "opp_half_pass_pct_zscore",

    # Per90 z-scores
    "assists_per90_zscore",
    "expectedassists_per90_zscore",
    "assists_minus_xa_per90_zscore",
    "goalsassistssum_per90_zscore",

    "totalpasses_per90_zscore",
    "accuratepasses_per90_zscore",
    "inaccuratepasses_per90_zscore",

    "totaloppositionhalfpasses_per90_zscore",
    "accurateoppositionhalfpasses_per90_zscore",

    "totalownhalfpasses_per90_zscore",
    "accurateownhalfpasses_per90_zscore",

    "accuratefinalthirdpasses_per90_zscore",

    "keypasses_per90_zscore",
    "totalattemptassist_per90_zscore",
    "passtoassist_per90_zscore",
    "bigchancescreated_per90_zscore",

    "totallongballs_per90_zscore",
    "accuratelongballs_per90_zscore",

    "totalchippedpasses_per90_zscore",
    "accuratechippedpasses_per90_zscore",

    "totalcross_per90_zscore",
    "accuratecrosses_per90_zscore",
]

possession_features = [
    # Raw percentages
    "successfuldribblespercentage",

    "dribbles_per_touch",
    "dispossessed_per_touch",
    "possession_lost_per_touch",

    # Percentage z-scores
    "successfuldribblespercentage_zscore",

    "dribbles_per_touch_zscore",
    "dispossessed_per_touch_zscore",
    "possession_lost_per_touch_zscore",

    # Per90 z-scores
    "touches_per90_zscore",
    "possessionwonattthird_per90_zscore",
    "possessionlost_per90_zscore",
    "dispossessed_per90_zscore",
    "totalcontest_per90_zscore",
    "successfuldribbles_per90_zscore",
    "offsides_per90_zscore",
    "wasfouled_per90_zscore",
    "fouls_per90_zscore",
]

defending_features = [
    # Raw percentages
    "tackleswonpercentage",

    # Percentage z-scores
    "tackleswonpercentage_zscore",

    # Per90 z-scores
    "tackles_per90_zscore",
    "tackleswon_per90_zscore",
    "interceptions_per90_zscore",
    "ballrecovery_per90_zscore",
    "possessionwonattthird_per90_zscore",
    "clearances_per90_zscore",
    "blockedshots_per90_zscore",
    "dribbledpast_per90_zscore",
    "errorleadtoshot_per90_zscore",
    "errorleadtogoal_per90_zscore",

    "defensive_actions_per90_zscore",
]

duel_features = [
    # Raw percentages
    "totalduelswonpercentage",
    "groundduelswonpercentage",
    "aerialduelswonpercentage",

    # Percentage z-scores
    "totalduelswonpercentage_zscore",
    "groundduelswonpercentage_zscore",
    "aerialduelswonpercentage_zscore",

    # Per90 z-scores
    "totalduelswon_per90_zscore",
    "duellost_per90_zscore",
    "groundduelswon_per90_zscore",
    "aerialduelswon_per90_zscore",
    "aeriallost_per90_zscore",
]

goalkeeper_features = [
    # Per90 z-scores
    "saves_per90_zscore",
    "savescaught_per90_zscore",
    "savesparried_per90_zscore",

    "savedshotsfrominsidethebox_per90_zscore",
    "savedshotsfromoutsidethebox_per90_zscore",

    "runsout_per90_zscore",
    "successfulrunsout_per90_zscore",

    "goalkicks_per90_zscore",

    "punches_per90_zscore",
    "highclaims_per90_zscore",
    "crossesnotclaimed_per90_zscore",
]

discipline_features = [
    "yellowcards_per90_zscore",
    "yellowredcards_per90_zscore",
    "directredcards_per90_zscore",
    "owngoals_per90_zscore",
]


all_defined = (
    set(volume_cols)
    | set(rate_cols)
    | set(per90_cols)
    | set(volume_zscore_cols)
    | set(metadata_features)
    | set(general_features)
    | set(availability_features)
    | set(per90_zscore_cols)
    | set(rate_zscore_cols)
    | {c.replace("_zscore", "") for c in volume_zscore_cols}
)

import pandas as pd

df=pd.read_csv('D:/FOOTBALL PROJECT/data/processed/major_leagues/Sofascore_player_data_2526.csv')

missing = sorted(set(df.columns) - all_defined)
print(missing)
