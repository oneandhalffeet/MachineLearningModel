# MachineLearningModel
XGBoost model for prediction of tear strength of fabric using fabric paramters

### How to use
1. Download anaconda and python
2. Download "APP File" folder
3. Go inside the folder via anaconda prompt
4. Write "pip install -r requirements.txt". and hit Enter
5. This will install all necessary module required
6. Write "python Input_file.py", hit Enter
7. GUI will open, input fabric parameters and Test it
8. It will output the predicted tear strength for both directions.
9. Input parameters need for prediction is 

a. thread count(expected) { if this is not available you can use actual thread count}
  
b. weave of fabric (1 for plain, 2 for satin)
  
c. finishing sequence of fabric {in our input data we have 5 finishing sequences which are, dyed, white dyed, pigment print, r. dyed and dyed over print}
  
d. blend % { we used % of cotton in the blend as a parameter}
  
e. warp and weft count
  
f. EPI and PPI
  
g. Actual thread count{thread count expected will suffice}
  
f. GSM of fabric
