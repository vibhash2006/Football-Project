metadata_features = [
    "player",
    "team",
    "player id",
    "team id",
    "league",
    "season",
    "position",
]

general_features = [
    "appearances",
    "matchesStarted",
    "minutesPlayed",
    "rating",
    "totalRating",
    "countRating",
    "totwAppearances",
]

attacking_features = [
    # Goals & Underlying Metrics
    "goals",
    "expectedGoals",
    "goalsAssistsSum",
    "goals_minus_xg",
    "goals_per_xg",
    "scoringFrequency",
    
    # Shooting & Box Proximity Volume
    "totalShots",
    "shotsOnTarget",
    "shotsOffTarget",
    "shotsFromInsideTheBox",
    "shotsFromOutsideTheBox",
    "shotFromSetPiece",
    "hitWoodwork",
    "goalConversionPercentage",
    'weak_foot_goals_pct',
    "setPieceConversion",
    "shots_on_target_pct",
    "inside_box_shot_pct",
    
    # Goal Subtypes
    "leftFootGoals",
    "rightFootGoals",
    "headedGoals",
    "goalsFromInsideTheBox",
    "goalsFromOutsideTheBox",
    "freeKickGoal",
    "penaltyGoals",
    
    # Penalties Taken
    "penaltiesTaken",
    "penaltyConversion",
    
    # Big Chance Efficiency
    "bigChancesMissed",
    
    # Attacking Per 90 Metrics
    "goals_per90",
    "expectedGoals_per90",
    "totalShots_per90",
    "shotsOnTarget_per90",
    "shotsOffTarget_per90",
    "shotsFromInsideTheBox_per90",
    "shotsFromOutsideTheBox_per90",
    "hitWoodwork_per90",
    "leftFootGoals_per90",
    "rightFootGoals_per90",
    "headedGoals_per90",
    "goalsFromInsideTheBox_per90",
    "goalsFromOutsideTheBox_per90",
    "freeKickGoal_per90",
    "penaltiesTaken_per90",
    "penaltyGoals_per90",
    "bigChancesMissed_per90",
]

creation_features = [
    # Output & Underlying Overperformance
    "assists",
    "expectedAssists",
    "assists_minus_xa",
    
    # Primary Chance Creation & Line Breaking
    "keyPasses",
    "totalAttemptAssist",
    "passToAssist",
    "bigChancesCreated",
    
    # General Passing Volume & Accuracy
    "totalPasses",
    "accuratePasses",
    "inaccuratePasses",
    "accuratePassesPercentage",
    
    # Passing Direction & Distance Subtypes
    "totalOppositionHalfPasses",
    "accurateOppositionHalfPasses",
    "totalOwnHalfPasses",
    "accurateOwnHalfPasses",
    "accurateFinalThirdPasses",
    "totalLongBalls",
    "accurateLongBalls",
    "accurateLongBallsPercentage",
    "totalChippedPasses",
    "accurateChippedPasses",
    "totalCross",
    "accurateCrosses",
    "accurateCrossesPercentage",
    
    # Creation Efficiency Ratios
    "assist_conversion",
    "xa_per_keypass",
    "final_third_pass_pct",
    "opp_half_pass_pct",
    
    # Creation Per 90 Metrics
    "assists_per90",
    "expectedAssists_per90",
    "goalsAssistsSum_per90",
    "totalPasses_per90",
    "accuratePasses_per90",
    "inaccuratePasses_per90",
    "totalOppositionHalfPasses_per90",
    "accurateOppositionHalfPasses_per90",
    "totalOwnHalfPasses_per90",
    "accurateOwnHalfPasses_per90",
    "accurateFinalThirdPasses_per90",
    "keyPasses_per90",
    "totalAttemptAssist_per90",
    "passToAssist_per90",
    "bigChancesCreated_per90",
    "totalLongBalls_per90",
    "accurateLongBalls_per90",
    "totalChippedPasses_per90",
    "accurateChippedPasses_per90",
    "totalCross_per90",
    "accurateCrosses_per90",
]

possession_features = [
    # Ball Retention Volume & Security
    "touches",
    "possessionLost",
    "dispossessed",
    
    # Dribbling & Individual Actions
    "totalContest",
    "successfulDribbles",
    "successfulDribblesPercentage",
    
    # In-Possession Match Events
    "offsides",
    "wasFouled",
    "fouls",
    
    # Possession Density Ratios
    "dribbles_per_touch",
    "dispossessed_per_touch",
    "possession_lost_per_touch",
    
    # Possession Per 90 Metrics
    "touches_per90",
    "possessionLost_per90",
    "dispossessed_per90",
    "totalContest_per90",
    "successfulDribbles_per90",
    "offsides_per90",
    "wasFouled_per90",
    "fouls_per90",
]

defending_features = [
    # Tackling Metrics
    "tackles",
    "tacklesWon",
    "tacklesWonPercentage",
    
    # Intercepting & Anticipation Metrics
    "interceptions",
    "ballRecovery",
    
    # Pressing Interventions
    "possessionWonAttThird",
    
    # Rescuing Defending Volume
    "clearances",
    "blockedShots",
    
    # Defending Flaws / Fragility
    "dribbledPast",
    "errorLeadToShot",
    "errorLeadToGoal",
    
    # Composite Calculations
    "defensive_actions",
    "defensive_actions_per90",
    
    # Defending Per 90 Metrics
    "tackles_per90",
    "tacklesWon_per90",
    "interceptions_per90",
    "ballRecovery_per90",
    "possessionWonAttThird_per90",
    "clearances_per90",
    "blockedShots_per90",
    "dribbledPast_per90",
    "errorLeadToShot_per90",
    "errorLeadToGoal_per90",
]

duel_features = [
    # General Duel Yields
    "totalDuelsWon",
    "totalDuelsWonPercentage",
    "duelLost",
    
    # Ground Battles
    "groundDuelsWon",
    "groundDuelsWonPercentage",
    
    # Aerial Battles
    "aerialDuelsWon",
    "aerialDuelsWonPercentage",
    "aerialLost",
    
    # Duel Per 90 Metrics
    "totalDuelsWon_per90",
    "duelLost_per90",
    "groundDuelsWon_per90",
    "aerialDuelsWon_per90",
    "aerialLost_per90",
]

goalkeeper_features = [
    # Clean Sheet Trackers
    "cleanSheet",
    
    # Conceding Parameters
    "goalsConceded",
    "goalsConcededInsideTheBox",
    "goalsConcededOutsideTheBox",
    
    # Basic & Complex Stopping
    "saves",
    "savesCaught",
    "savesParried",
    "savedShotsFromInsideTheBox",
    "savedShotsFromOutsideTheBox",
    "goalsPrevented",
    
    # Box Management & Claiming
    "punches",
    "highClaims",
    "crossesNotClaimed",
    
    # Sweeping / Mobility Out of Box
    "runsOut",
    "successfulRunsOut",
    "goalKicks",
    
    # Penalty-Faced Interventions
    "penaltyFaced",
    "penaltySave",
    "penaltyConceded",
    "penaltyWon",
    "attemptPenaltyMiss",
    "attemptPenaltyTarget",
    "attemptPenaltyPost",
]

discipline_features = [
    # General Booking Volumes & Direct Blunders
    "yellowCards",
    "yellowRedCards",
    "directRedCards",
    "redCards",
    "ownGoals",
    
    # Booking & Self-Sabotage Per 90 Metrics
    "yellowCards_per90",
    "yellowRedCards_per90",
    "directRedCards_per90",
    "ownGoals_per90",
    
]

