from utils.general import labels_to_class_weights, increment_path, labels_to_image_weights, init_seeds, \
    fitness, strip_optimizer, get_latest_run, check_dataset, check_file, check_git_status, check_img_size, \
    check_requirements, print_mutation, set_logging, one_cycle, colorstr
from utils.plots import plot_images, plot_labels, plot_results, plot_evolution
from opts import opts
import yaml
from pathlib import Path
import math
import numpy as np
import random
import time
def training_model(number):


    output1 = -(number**2)
  

   
    print("This is result:"+str(output1))

    return output1
if __name__ == '__main__':
    
    opt = opts().parse()
    
    number = opt.number

    if opt.evolve == 'False' :    

        output1 = training_model(number)
    
    else:

        if Path(opt.hyp).exists() ==False:

            with open(opt.hyp, 'w') as f:

                default  = {'number':opt.number}

                for k,v in default.items():
                    f.write(str(k)+": "+str(v)+ "\n")
      
        with open(opt.hyp) as f:
            
            hyp = yaml.safe_load(f)  # load hyps

            meta = { 'number':(1,0,opt.number) }

        yaml_file = Path('/home/ackd06/hyp_evolution/') / 'hyp_evolved.yaml'  # save best result here    

        for epoch in range(600):
            print(epoch)
            if Path('evolve.txt').exists():  # if evolve.txt exists: select best hyps and mutate              
                
                # Select parent(s)
                parent = 'single'  # parent selection method: 'single' or 'weighted'
                x = np.loadtxt('evolve.txt', ndmin=2)
                n = min(3, len(x))  # number of previous results to consider
                x = x[np.argsort(-fitness(x))][:n]  # top n mutations
                w = fitness(x) - fitness(x).min()  # weights
                if parent == 'single' or len(x) == 1:
                    # x = x[random.randint(0, n - 1)]  # random selection
                    x = x[random.choices(range(n), weights=w)[0]]  # weighted selection
                elif parent == 'weighted':
                    x = (x * w.reshape(n, 1)).sum(0) / w.sum()  # weighted combination
               
                # Mutate
                mp, s = 0.8, 0.2 # mutation probability, sigma
                npr = np.random
                npr.seed(int(time.time()))
                g = np.array([x[0] for x in meta.values()]) 
                ng = len(meta)
                v = np.ones(ng)
                while all(v == 1):  # mutate until a change occurs (prevent duplicates)
                    v = (g * (npr.random(ng) < mp) * npr.randn(ng) * npr.random() * s + 1).clip(0.3, 3.0)
                
                for i, k in enumerate(hyp.keys()):  # plt.hist(v.ravel(), 300)

                     hyp[k] = float(x[i + 1 ] * v[i])
         
                for k, v in meta.items():
                 
                    hyp[k] = max(hyp[k], v[1])  # lower limit
               
                    hyp[k] = min(hyp[k], v[2])  # upper limit

                    hyp[k] = round(hyp[k], 5)  # significant digits     

                    number = hyp['number']

            output1 = training_model(number)
            print('output: %f' %(output1))
            results = (output1,)
                 
   
            print_mutation(hyp, results, yaml_file)

        plot_evolution(yaml_file)  

