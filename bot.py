# @mrlokaman ©️ shyan
#lntechnical
import os
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from googletrans import Translator
TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", 12345))

API_HASH = os.environ.get("API_HASH", "")
app = Client(
        "Gtt",
        bot_token=TOKEN,api_hash=API_HASH,
            api_id=API_ID
    )

@app.on_message(filters.private & filters.command(['start']))
async def start(client, message):
	await message.reply_text(text =f"Hello **{message.from_user.first_name }** \n\n __I am simple Google Translater Bot \n I can translate any language to you selected language__",reply_to_message_id = message.message_id ,parse_mode="markdown", reply_markup=InlineKeyboardMarkup([ [                    InlineKeyboardButton("Support 🇮🇳" ,url="https://t.me/lntechnical") ],               [InlineKeyboardButton("Subscribe 🧐", url="https://youtube.com/c/LNtechnical") ]   ]  ) )
                  



@app.on_message(filters.private & filters.text  )
async def echo(client, message):

 
 keybord1= InlineKeyboardMarkup( [
        [ 
            InlineKeyboardButton("Afrikaans", callback_data='af'),
             InlineKeyboardButton("Albanian", callback_data='sq'),
            InlineKeyboardButton("Amharic",callback_data ='am'),
        ],
        [   InlineKeyboardButton("Arabic", callback_data='ar'),
        InlineKeyboardButton("Armenian", callback_data='hy'),      
        InlineKeyboardButton("Azerbaijani",callback_data = 'az'),        
        ],
        [InlineKeyboardButton("Basque",callback_data ="eu"),
        	 InlineKeyboardButton("Belarusian",callback_data ="be"),       	
	InlineKeyboardButton("Bengali",callback_data="bn")],
	
	[InlineKeyboardButton("Bosnian",callback_data = "bs"),
	InlineKeyboardButton("Bulgarian",callback_data ="bg"),
	InlineKeyboardButton("Catalan",callback_data = "ca")
	],
	[ 
	InlineKeyboardButton("Corsican",callback_data ="co"),
	InlineKeyboardButton("Croatian",callback_data = "hr"),
	InlineKeyboardButton("Czech", callback_data = "cs"),
	],
	[ InlineKeyboardButton("Danish",callback_data = "da"),
	InlineKeyboardButton("Dutch",callback_data = "nl"),
	InlineKeyboardButton("Esperanto",callback_data = "eo"),	 
	],
	[InlineKeyboardButton(" Next --->",callback_data = "page2")
	]
	] )
	
 await  message.reply_text("Select language 👇",reply_to_message_id = message.message_id, reply_markup = keybord1) 


@app.on_callback_query()
async def translate_text(bot,update):
  keybord6 =  InlineKeyboardMarkup([
       [InlineKeyboardButton("Thai",callback_data = "th"),
       InlineKeyboardButton("Turkish",callback_data = "tr"),
       InlineKeyboardButton("Turkmen",callback_data ="tk")     
       ],
       [InlineKeyboardButton("Ukrainian",callback_data = "uk"),
       InlineKeyboardButton("Urdu",callback_data = "ur"),
       InlineKeyboardButton("Uyghur",callback_data ="ug")
       
       ],
       [InlineKeyboardButton("Uzbek",callback_data = "uz"),
       InlineKeyboardButton("Vietnamese",callback_data ="vi"),
       InlineKeyboardButton("Welsh",callback_data = "cy")
       
       ],
       [InlineKeyboardButton("Xhosa",callback_data = "xh"),
       InlineKeyboardButton("Yiddish",callback_data = "yi"),
       InlineKeyboardButton("Yoruba",callback_data = "yo")],
       [InlineKeyboardButton("<--- Back",callback_data = "page5")
       
       ]
 ])
  
  keybord5 = InlineKeyboardMarkup([
         [InlineKeyboardButton("Scots Gaelic",callback_data = "gd"),
         InlineKeyboardButton("Serbian",callback_data = "sr"),
         InlineKeyboardButton("Sesotho",callback_data = "st")
         ],
         [InlineKeyboardButton("Shona",callback_data ="sn"),
         InlineKeyboardButton("Sindhi",callback_data ="sd"),
         InlineKeyboardButton("Sinhala (Sinhalese)",callback_data = "si")
         ],
         [InlineKeyboardButton("Slovak",callback_data = "sk"),
         InlineKeyboardButton("Slovenian",callback_data = "sl"),
         InlineKeyboardButton("Somali",callback_data = "so")
         ],
         [InlineKeyboardButton("Spanish",callback_data = "es"),
         InlineKeyboardButton("Sundanese",callback_data ="su"),
         InlineKeyboardButton("Swahili",callback_data ="sw")
         ],
         [InlineKeyboardButton("Swedish",callback_data = "sv"),
         InlineKeyboardButton("Tagalog (Filipino)",callback_data ='tl'),
         InlineKeyboardButton("Tajik",callback_data = "tg")
         ],
         [InlineKeyboardButton("Tamil",callback_data = "ta"),
         InlineKeyboardButton("Tatar",callback_data = "tt"),
         InlineKeyboardButton("Telugu",callback_data = "te")
         ],
         [InlineKeyboardButton("<--- Back",callback_data = "page4"),
         InlineKeyboardButton("Next --->",callback_data = "page6")
         ]  ])
   
 
  keybord4 = InlineKeyboardMarkup([
          [InlineKeyboardButton("Malayalam",callback_data = "ml"),
          InlineKeyboardButton("Maltese",callback_data = "mt"),
          InlineKeyboardButton("Maori",callback_data = "mi")
          ],
          [InlineKeyboardButton("Marathi",callback_data = "mr"),
          InlineKeyboardButton("Mongolian",callback_data = "mn"),
          InlineKeyboardButton("Myanmar (Burmese)",callback_data = "my")
          ],
          [InlineKeyboardButton("Nepali",callback_data ="ne"),
          InlineKeyboardButton("Norwegian",callback_data = "no"),
          InlineKeyboardButton("Nyanja (Chichewa)",callback_data = "ny")
          ],
          [InlineKeyboardButton("Odia",callback_data = "or"),
          InlineKeyboardButton("Pashto",callback_data = "ps"),
          InlineKeyboardButton("Persian",callback_data = "fa"),
          ],
          [InlineKeyboardButton("Polish",callback_data = "pl"),
          InlineKeyboardButton("Portuguese",callback_data = "pt"),
          InlineKeyboardButton("Punjabi",callback_data = "pa"),
          ],
          [InlineKeyboardButton("Romanian",callback_data = "ro"),
          InlineKeyboardButton("Russian",callback_data = "ru"),
          InlineKeyboardButton("Samoan",callback_data= "sm"),
          ],
          [InlineKeyboardButton("<--- Back",callback_data = "page3"),
          InlineKeyboardButton("Next --->",callback_data = "page5")
          ]
          
 
 
 
 ])
  
  
  keybord3 = InlineKeyboardMarkup([
                [ InlineKeyboardButton("Italian",callback_data = "it"),
                InlineKeyboardButton("Japanese",callback_data = "ja"),
                InlineKeyboardButton("Javanese",callback_data = "jv")
                ],
                [InlineKeyboardButton("Kannada",callback_data = "kn"),
                InlineKeyboardButton("Kazakh",callback_data = "kk"),
                InlineKeyboardButton("Khmer",callback_data = "km")
                ],
                [InlineKeyboardButton("Kinyarwanda",callback_data = "rw"),
                InlineKeyboardButton("Korean",callback_data ="ko"),
                InlineKeyboardButton("Kurdish",callback_data = "ku")
                ],
                [ InlineKeyboardButton("Kyrgyz",callback_data ="ky"),
                InlineKeyboardButton("Lao",callback_data = "lo"),
                InlineKeyboardButton("Latin",callback_data = "la")
                ],
                [InlineKeyboardButton("Latvian",callback_data = "lv"),
                InlineKeyboardButton('Lithuanian',callback_data ="lt"),
                InlineKeyboardButton("Luxembourgish",callback_data = "lb")
                ],
                [InlineKeyboardButton("Macedonian",callback_data = "mk"),
                InlineKeyboardButton("Malagasy",callback_data ="mg"),
                InlineKeyboardButton("Malay",callback_data ="ms")
                ],
                [InlineKeyboardButton("<--- Back",callback_data = "page2"),
                InlineKeyboardButton(" Next --->",callback_data = "page4")
                ]
              
 
 ])
  
  
  keybord1= InlineKeyboardMarkup( [
        [ 
            InlineKeyboardButton("Afrikaans", callback_data='af'),
             InlineKeyboardButton("Albanian", callback_data='sq'),
            InlineKeyboardButton("Amharic",callback_data ='am'),
        ],
        [   InlineKeyboardButton("Arabic", callback_data='ar'),
        InlineKeyboardButton("Armenian", callback_data='hy'),      
        InlineKeyboardButton("Azerbaijani",callback_data = 'az'),        
        ],
        [InlineKeyboardButton("Basque",callback_data ="eu"),
        	 InlineKeyboardButton("Belarusian",callback_data ="be"),       	
	InlineKeyboardButton("Bengali",callback_data="bn")],
	
	[InlineKeyboardButton("Bosnian",callback_data = "bs"),
	InlineKeyboardButton("Bulgarian",callback_data ="bg"),
	InlineKeyboardButton("Catalan",callback_data = "ca")
	],
	[ 
	InlineKeyboardButton("Corsican",callback_data ="co"),
	InlineKeyboardButton("Croatian",callback_data = "hr"),
	InlineKeyboardButton("Czech", callback_data = "cs"),
	],
	[ InlineKeyboardButton("Danish",callback_data = "da"),
	InlineKeyboardButton("Dutch",callback_data = "nl"),
	InlineKeyboardButton("Esperanto",callback_data = "eo"),	 
	],
	[InlineKeyboardButton(" Next --->",callback_data = "page2")
	]
	] )
  
  
  keybord2= InlineKeyboardMarkup([
           [InlineKeyboardButton("English",callback_data = "en"),
           InlineKeyboardButton("Estonian",callback_data = "et"),
           InlineKeyboardButton("Finnish",callback_data = "fi")
           ],
           [InlineKeyboardButton("French",callback_data = "fr"),
           InlineKeyboardButton("Frisian",callback_data = "fy"),
           InlineKeyboardButton("Galician",callback_data = "gl")
           ],
           [InlineKeyboardButton("Georgian",callback_data = "ka"),
           InlineKeyboardButton("German",callback_data = "de"),
           InlineKeyboardButton("Greek",callback_data = "el")
           ],
           [InlineKeyboardButton("Gujarati",callback_data = "gu"),
           InlineKeyboardButton("Haitian Creole",callback_data = "ht"),
           InlineKeyboardButton("Hausa",callback_data ="ha")
           ],
           [InlineKeyboardButton("Hindi",callback_data = "hi"),
           InlineKeyboardButton("Hungarian",callback_data = "hu"),
           InlineKeyboardButton("Icelandic",callback_data = "is")
           ],
           [InlineKeyboardButton("Igbo",callback_data = "ig"),
           InlineKeyboardButton("Indonesian",callback_data = "id"),
           InlineKeyboardButton("Irish",callback_data = "ga")
           ],
           [InlineKeyboardButton("<--- Back",callback_data = "page1"),
           InlineKeyboardButton(" Next --->",callback_data = "page3"),
           ]
            ])
						
  
  
  
  tr_text = update.message.reply_to_message.text
  cb_data = update.data
  if cb_data== "page2":
  	await update.message.edit("Select language 👇",reply_markup = keybord2)
  elif cb_data == "page1":
  	await update.message.edit("Select language 👇",reply_markup =keybord1)
  elif cb_data =="page3":
  	await update.message.edit("Select language 👇",reply_markup =keybord3)
  elif cb_data == "page4":
  	await update.message.edit("Select language 👇",reply_markup =keybord4)
  elif cb_data =="page5":
  	await update.message.edit("Select language 👇",reply_markup =keybord5)
  elif cb_data =="page6":
  	await update.message.edit("Select language 👇",reply_markup =keybord6)
  else :
       translator = Translator()  
       translation = translator.translate(tr_text,dest=cb_data) 
       await update.message.edit(translation.text)

app.run()
