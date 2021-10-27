# hyp_evolution
![image](https://github.com/ITRI-ICLX-DNN/hyp_evolution/blob/main/flowchart.png)

## 1.各個檔案說明

   hyp.scratch.yaml <-----  預設的參數設定檔案(第一次訓練模型，由這裡設定參數)<br>
   hyp_evolved.yaml <-----  最佳參數，以及最佳結果存在這個檔案中 (metrics 順序依序為最佳結果，以及最佳參數)<br>
   evolve.txt       <-----  找參數的訓練結果過程，排列順序會由最佳到最差的結果<br>
## 2.根據需求修改

   training.py      <----- 輸出的結果為一項，所以讀取值時，為i+1<br>
   
![image](https://github.com/ITRI-ICLX-DNN/hyp_evolution/blob/main/1.JPG)

utils/metrics.py  <-----  根據輸出的結果，為結果賦予權重
為了方便舉例，使用下方範例圖，下方範例圖非此code的內容，下方的例子為有四個輸出分別為precision、recall、mAP@0.5、mAP@0.95，分別賦予這四個output各自的權重在做加總，在此code中只有一項output ，所以權重設為1在做加總即可<br>
![image](https://github.com/ITRI-ICLX-DNN/hyp_evolution/blob/main/2.JPG)

utils/general.py
![image](https://github.com/ITRI-ICLX-DNN/hyp_evolution/blob/main/3.JPG)


結果保存在evolve.png，下方每一個圖代表一個Hyperparameter。參數當前值對應在 x 軸上，fitness對應在 y 上。
最佳的參數保存在hyp_evolved.yaml檔案中<br>

![image](https://github.com/ITRI-ICLX-DNN/hyp_evolution/blob/main/evolve.png)
