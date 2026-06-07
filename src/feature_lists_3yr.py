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
    "totwappearances",
]

attacking_features = [
    # Goals & Underlying Metrics
    "goals",
    "expectedgoals",
    "goalsassistssum",
    "goals_minus_xg",
    "goals_per_xg",
    
    # Shooting & Box Proximity Volume
    "totalshots",
    "shotsontarget",
    "shotsofftarget",
    "shotsfrominsidethebox",
    "shotsfromoutsidethebox",
    "shotfromsetpiece",
    "hitwoodwork",
    "goalconversionpercentage",
    "weak_foot_goals_pct",
    "setpiececonversion",
    "shots_on_target_pct",
    "inside_box_shot_pct",
    "attemptpenaltymiss",
    "attemptpenaltypost",
    "attemptpenaltytarget",
    
    
    # Goal Subtypes
    "leftfootgoals",
    "rightfootgoals",
    "headedgoals",
    "goalsfrominsidethebox",
    "goalsfromoutsidethebox",
    "freekickgoal",
    "penaltygoals",
    
    # Penalties Taken
    "penaltiestaken",
    "penaltyconversion",
    
    # Big Chance Efficiency
    "bigchancesmissed",
    
    # Attacking Per 90 Metrics
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
]

creation_features = [
    # Output & Underlying Overperformance
    "assists",
    "expectedassists",
    "assists_minus_xa",
    
    # Primary Chance Creation & Line Breaking
    "keypasses",
    "totalattemptassist",
    "passtoassist",
    "bigchancescreated",
    
    # General Passing Volume & Accuracy
    "totalpasses",
    "accuratepasses",
    "inaccuratepasses",
    "accuratepassespercentage",
    
    # Passing Direction & Distance Subtypes
    "totaloppositionhalfpasses",
    "accurateoppositionhalfpasses",
    "totalownhalfpasses",
    "accurateownhalfpasses",
    "accuratefinalthirdpasses",
    "totallongballs",
    "accuratelongballs",
    "accuratelongballspercentage",
    "totalchippedpasses",
    "accuratechippedpasses",
    "totalcross",
    "accuratecrosses",
    "accuratecrossespercentage",
    
    # Creation Efficiency Ratios
    "assist_conversion",
    "xa_per_keypass",
    "final_third_pass_pct",
    "opp_half_pass_pct",
    
    # Creation Per 90 Metrics
    "assists_per90",
    "expectedassists_per90",
    "assists_minus_xa_per90"
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
]

possession_features = [
    # Ball Retention Volume & Security
    "touches",
    "possessionwonattthird",
    "possessionlost",
    "dispossessed",
    
    # Dribbling & Individual Actions
    "totalcontest",
    "successfuldribbles",
    "successfuldribblespercentage",
    
    # In-Possession Match Events
    "offsides",
    "wasfouled",
    "fouls",
    
    # Possession Density Ratios
    "dribbles_per_touch",
    "dispossessed_per_touch",
    "possession_lost_per_touch",
    
    # Possession Per 90 Metrics
    "touches_per90",
    "possessionwonattthird_per90",
    "possessionlost_per90",
    "dispossessed_per90",
    "totalcontest_per90",
    "successfuldribbles_per90",
    "offsides_per90",
    "wasfouled_per90",
    "fouls_per90",
]

defending_features = [
    # Tackling Metrics
    "tackles",
    "tackleswon",
    "tackleswonpercentage",
    
    # Intercepting & Anticipation Metrics
    "interceptions",
    "ballrecovery",
    
    # Pressing Interventions
    "possessionwonattthird",
    
    # Rescuing Defending Volume
    "clearances",
    "blockedshots",
    
    # Defending Flaws / Fragility
    "dribbledpast",
    "errorleadtoshot",
    "errorleadtogoal",
    
    # Composite Calculations
    "defensive_actions",
    "defensive_actions_per90",
    
    # Defending Per 90 Metrics
    "tackles_per90",
    "tackleswon_per90",
    "interceptions_per90",
    "ballrecovery_per90",
    "possessionwonattthird_per90",
    "clearances_per90",
    "blockedshots_per90",
    "dribbledpast_per90",
    "errorleadtoshot_per90",
    "errorleadtogoal_per90",
]

duel_features = [
    # General Duel Yields
    "totalduelswon",
    "totalduelswonpercentage",
    "duellost",
    
    # Ground Battles
    "groundduelswon",
    "groundduelswonpercentage",
    
    # Aerial Battles
    "aerialduelswon",
    "aerialduelswonpercentage",
    "aeriallost",
    
    # Duel Per 90 Metrics
    "totalduelswon_per90",
    "duellost_per90",
    "groundduelswon_per90",
    "aerialduelswon_per90",
    "aeriallost_per90",
]

goalkeeper_features = [
    # Clean Sheet Trackers
    "cleansheet",
    
    # Conceding Parameters
    "goalsconceded",
    "goalsconcededinsidethebox",
    "goalsconcededoutsidethebox",
    
    # Basic & Complex Stopping
    "saves",
    "savescaught",
    "savesparried",
    "savedshotsfrominsidethebox",
    "savedshotsfromoutsidethebox",
    "goalsprevented",
    
    # Box Management & Claiming
    "punches",
    "highclaims",
    "crossesnotclaimed",
    
    # Sweeping / Mobility Out of Box
    "runsout",
    "successfulrunsout",
    "goalkicks",
    
    # Penalty-Faced Interventions
    "penaltyfaced",
    "penaltysave",
    "penaltyconceded",
    "penaltywon",
    "attemptpenaltymiss",
    "attemptpenaltytarget",
    "attemptpenaltypost",
    
    # Goalkeeping per 90 Metrics
    "saves_per90",
    "savescaught_per90",
    "savesparried_per90",
    "savedshotsfrominsidethebox_per90",
    "savedshotsfromoutsidethebox_per90",
    "goalsprevented_per90",
    "runsout_per90",
    "successfulrunsout_per90",
    "goalkicks_per90",
    "punches_per90",
    "highclaims_per90",
    "crossesnotclaimed_per90",
]

discipline_features = [
    # General Booking Volumes & Direct Blunders
    "yellowcards",
    "yellowredcards",
    "directredcards",
    "redcards",
    "owngoals",
    
    # Booking & Self-Sabotage Per 90 Metrics
    "yellowcards_per90",
    "yellowredcards_per90",
    "directredcards_per90",
    "owngoals_per90",
]