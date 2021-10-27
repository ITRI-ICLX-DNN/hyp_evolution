# hyp_evolution
![image](https://github.com/ITRI-ICLX-DNN/hyp_evolution/blob/main/flowchart.png)

1.各個檔案說明

   hyp.scratch.yaml <-----  預設的參數設定檔案(第一次訓練模型，由這裡設定參數)
   hyp_evolved.yaml <-----  最佳參數，以及最佳結果存在這個檔案中 (metrics 順序依序為最佳結果，以及最佳參數)
   evolve.txt       <-----  找參數的訓練結果過程，排列順序會由最佳到最差的結果
