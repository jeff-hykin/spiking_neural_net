import argparse

ARGS_HELPER = {}
def args_maker(args_dict):
    global ARGS_HELPER
    ARGS_HELPER = args_dict
    return """
parser = argparse.ArgumentParser()
for each in ARGS_HELPER.keys():
    parser.add_argument(f'--{each}', **ARGS_HELPER[each])
args = parser.parse_args()
keys = args.__dir__()
for each in ARGS_HELPER.keys():
    if each in keys:
        exec(f"{each} = args.{each}")
    """

    

exec(args_maker({
    "seed":              { "type" : int    , "default" : 0             },
    "n_neurons":         { "type" : int    , "default" : 100           },
    "n_epochs":          { "type" : int    , "default" : 1             },
    "n_test":            { "type" : int    , "default" : 10000         },
    "n_workers":         { "type" : int    , "default" : -1            },
    "exc":               { "type" : float  , "default" : 22.5          },
    "inh":               { "type" : float  , "default" : 120           },
    "theta_plus":        { "type" : float  , "default" : 0.05          },
    "time":              { "type" : int    , "default" : 250           },
    "dt":                { "type" : int    , "default" : 1.0           },
    "intensity":         { "type" : float  , "default" : 128           },
    "progress_interval": { "type" : int    , "default" : 10            },
    "update_interval":   { "type" : int    , "default" : 250           },
    "train":             { "dest" : "train", "action"  : "store_true"  },
    "test":              { "dest" : "train", "action"  : "store_false" },
    "plot":              { "dest" : "plot" , "action"  : "store_true"  },
    "gpu":               { "dest" : "gpu"  , "action"  : "store_true"  },
}))

print(gpu)