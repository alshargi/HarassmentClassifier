
# -*- coding: utf-8 -*-
# Done By 
## Dr. Faisal ALSHARGI
## New York, US, Aug 16, 2023
##############################

import joblib
import pandas as pd

dict_locs = {} 

Haras_label = { 0: 'Appearance',1: 'Cussing',
                2: 'Intellectual',3: 'NOT',
                4: 'Political', 5: 'Racial', 
                6: 'Religion',7: 'Sexual',
                8: 'Violence'}

labels_info_haras = ['Appearance', 'Cussing', 'Intellectual', 'NOT', 
                    'Political','Racial','Religion', 'Sexual','Violence']

dict_locs = {} 

### load models
loaded_calibrated_svc_Main = joblib.load('haras/haras_svc_model.sav')
loaded_count_vect_Main = joblib.load('haras/haras_count_vect_model.sav')
loaded_tf_transformer_Main = joblib.load('haras/haras_tfidf_transformer_model.sav')
loaded_label_encoder_Main = joblib.load('haras/haras_label_encoder_model.sav')
print("Harassment models, Loaded")




def get_pred_main(to_predict):
    keepres = []
    p_count = loaded_count_vect_Main.transform(to_predict)
    p_tfidf = loaded_tf_transformer_Main.transform(p_count)
    themax = loaded_calibrated_svc_Main.predict(p_tfidf)              
    dres = pd.DataFrame(loaded_calibrated_svc_Main.predict_proba(p_tfidf)*100 , columns=loaded_label_encoder_Main.classes_ )
    for content in dres.items():
        dict_locs[Haras_label[content[0]]]=  content[1][0]
    sorted_val = sorted(dict_locs.items(), key = lambda kv: kv[1] , reverse = 1)
    for i in sorted_val:
        keepres.append("{}\t{}".format(i[0], str(round(i[1], 3)) ))
    return str(labels_info_haras[themax[0]]), keepres



def findres(X_new):
    X_new_counts = loaded_count_vect_Main.transform(X_new)
    X_new_transformed = loaded_tf_transformer_Main.transform(X_new_counts)
    predicted_new = loaded_calibrated_svc_Main.predict(X_new_transformed)
    predicted_labels_original = loaded_label_encoder_Main.inverse_transform(predicted_new)
    return X_new, Haras_label[predicted_labels_original[0]]

#################
def get_pred_label(to_predict):
    keepallFinal = []
    for tx in to_predict:
        maxres, res_main = get_pred_main([tx])
        keepallFinal.append("{}\tMax Result:{}".format(tx,res_main))

            
    return keepallFinal




