""" use this file for creating project structure overall configuration of project  """
import os, sys

CFG={
        "data": 
        {
            "data_dir": "D:\Learning Projects\skyline project\week1_Text_Classification\youtube_video_comments"
        },
        "data_preprocessing": 
        {
            "Column": "CONTENT", 
            "preprocessing_steps": 
            { 
                "remove_punctuations": True,
                "remove_stopwords": True,
                "remove_numbers": True,
                "remove_emojis": True,
                "remove_urls": True,
                "remove_html_tags": True,
                "remove_extra_spaces": True,
                "convert_to_lowercase": True,
                "lemmatize": True,
                "remove_words_with_length_less_than_2 and greater_than_15": True
            }
        }

}

print(CFG['data_preprocessing']['Column'])