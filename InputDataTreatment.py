# simulation settings
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50     # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03     # annual discount rate
DELTA_T = 1         # years

# transition matrix
TRANS_MATRIX = [
    [0.7500,   0.1500,  0.0000,   0.1000],   #WELL
    [0.0000,   0.0000,  1.0000,   0.0000],   #STROKE
    [0.0000,   0.1625,  0.7010,   0.1365],   #POST STROKE
    [0.0000,   0.0000,  0.0000,   1.0000],   #DEATH
]

# annual cost of each health state
ANNUAL_STATE_COST = [
    0.0,      # WELL
    5000.0,   # STROKE
    2000.0    # POST STROKE
    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    0.75,   # WELL
    0.50,   # STROKE
    0.25    # POST STROKE
    ]

# annual drug costs
NOTHERAPY_COST = 100.0
ANTICOAG_COST = 2000.0


