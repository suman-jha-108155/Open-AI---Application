import tkinter as tk
import os
import json
import openai
from gpt import GPT
from gpt import Example

WIDTH=700
HEIGHT=500

def main():
	window = tk.Tk()

	##########################################SQL QUERY ###############################################################
	def sqlquery():
		root=tk.Tk()

		def clear():
			entry.delete(0, tk.END)
			text.delete('1.0', tk.END)	

		def sqlquery2(query):
			openai.api_key = "your-api-key"
			gpt = GPT(engine="davinci", temperature=0.5, max_tokens=100)
			gpt.add_example(Example("fetch unique values of DEPARTMENT from worker table", 
					"Select distinct DEPARTMENT from worker;"))

			gpt.add_example(Example("fetch all the values from worker table", 
					"select * from worker;"))

			gpt.add_example(Example("print the first three charcters of FIRST_NAME from worker table", 
					"Select substring(FIRST_NAME,1,3) from worker;"))

			gpt.add_example(Example("Find the position of thhe alphabet ('a') in the first name column 'Amitabh' from worker table", 
					"Select CONCAT(FIRST_NAME, BINARY'a') from worker where FIRST_NAME = 'Amitabh';"))

			gpt.add_example(Example("Display the second highest salary from worker table", 
					"Select max(Salary)from worker where Salary not in (Select max(Salary) from worker);"))

			gpt.add_example(Example("Display the highest salary from worker table", 
					"Select max(Salary) from worker;"))

			gpt.add_example(Example("fetch the count of employees working in the department Admin", 
					"Select COUNT(*) FROM worker where DEPARTMENT = 'Admin';"))

			gpt.add_example(Example("Get all details of the Worers whose salary lies between 1000 and 5000", 
					"Select Salary from worker;"))

			gpt.add_example(Example("fetch all the values from worker table where name is suman", 
					"select * from worker where name ='suman';"))
			
			gpt.add_example(Example("fetch all the values from student table where name is mahima and binayak", 
					"select * from student where name ='suman' and name='binayak';"))
			
			prompt = query
			answer = gpt.get_top_reply(prompt)
			text.delete('1.0', tk.END)
			text.insert(tk.INSERT, answer)



		canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ccffff')
		canvas.pack(fill='both')

		frame = tk.Frame(root, bg='#1affff')
		frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

		entry= tk.Entry(frame, bg='white', font=15)
		entry.place(relx=0, rely=0.2, relwidth=0.8, relheight=0.1)

		label = tk.Label(frame, bg='#00cccc', text='Type Query in English : ', font=18)
		label.place(relx=0, rely=0.1, relwidth=0.8, relheight=0.1)

		button = tk.Button(frame, bg='#00cccc', text='Submit', font=18, command=lambda:sqlquery2(entry.get()))
		button.place(relx=0.8, rely=0.097, relwidth=0.2, relheight=0.1)

		button = tk.Button(frame, bg='#00cccc', text='Clear', font=18, command=clear)
		button.place(relx=0.8, rely=0.2, relwidth=0.2, relheight=0.1)

		label = tk.Label(frame, bg='#00cccc', text='Generated SQL Query is : ', font=18)
		label.place(relx=0, rely=0.5, relwidth=0.8, relheight=0.1)

		text = tk.Text(frame, bg='white', font=18)
		text.place(relx=0, rely=0.6, relwidth=0.8, relheight=0.3)

		root.mainloop()


	####################################################### QNA #############################################################

	def qna():

		root=tk.Tk()

		def clear():
			entry.delete(0, tk.END)
			text.delete('1.0', tk.END)	

		def questionans(question2):
			openai.api_key = "your-api-key"
	 
			document_list = ["Google was founded in 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. ,They incorporated Google as a privately held company on September 4, 1998. An initial public offering (IPO) took place on August 19, 2004, and Google moved to its headquarters in Mountain View, California, nicknamed the Googleplex. In August 2015, Google announced plans to reorganize its various interests as a conglomerate called Alphabet Inc. Google is Alphabet's leading subsidiary and will continue to be the umbrella company for Alphabet's Internet interests. Sundar Pichai was appointed CEO of Google, replacing Larry Page who became the CEO of Alphabet.",
			"Amazon is an American multinational technology company based in Seattle, Washington, which focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. It is one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Microsoft, and Facebook. The company has been referred to as 'one of the most influential economic and cultural forces in the world', as well as the world's most valuable brand. Jeff Bezos founded Amazon from his garage in Bellevue, Washington on July 5, 1994. It started as an online marketplace for books but expanded to sell electronics, software, video games, apparel, furniture, food, toys, and jewelry. In 2015, Amazon surpassed Walmart as the most valuable retailer in the United States by market capitalization."]
			
			response = openai.Answer.create(
			 	search_model="davinci",
			 	model="curie",
			 	question=question2,
			 	documents=document_list,
			 	examples_context="In 2017, U.S. life expectancy was 78.6 years.",
			 	examples=[["What is human life expectancy in the United States?","78 years."]],
			 	max_tokens=100,
			 	stop=["\n", "<|endoftext|>"],
				)

			result = json.loads(str(response))
			answer = result["answers"][0]
			text.delete('1.0', tk.END)
			text.insert(tk.INSERT, answer) 


		canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ccffff')
		canvas.pack(fill='both')

		frame = tk.Frame(root, bg='#1affff')
		frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

		entry= tk.Entry(frame, bg='white', font=15)
		entry.place(relx=0, rely=0.2, relwidth=0.8, relheight=0.1)

		label = tk.Label(frame, bg='#00cccc', text='Ask Any Question : ', font=18)
		label.place(relx=0, rely=0.1, relwidth=0.8, relheight=0.1)

		button = tk.Button(frame, bg='#00cccc', text='Submit', font=18, command=lambda:questionans(entry.get()))
		button.place(relx=0.8, rely=0.097, relwidth=0.2, relheight=0.1)

		button = tk.Button(frame, bg='#00cccc', text='Clear', font=18, command=clear)
		button.place(relx=0.8, rely=0.2, relwidth=0.2, relheight=0.1)

		label = tk.Label(frame, bg='#00cccc', text='Answer for the question is : ', font=18)
		label.place(relx=0, rely=0.5, relwidth=1, relheight=0.1)

		text = tk.Text(frame, bg='white', font=18)
		text.place(relx=0, rely=0.6, relwidth=1, relheight=0.4)

		root.mainloop()

	####################################################QNA ################################################################# 

	########################################### Paraphrasing ################################################################
	def paraphrasing():
		root=tk.Tk()

		def clear():
			entry.delete(0, tk.END)
			text.delete('1.0', tk.END)	

		def paraphrasinginterpretaion(phrase):
			openai.api_key = "your-api-key"

			start_sequence = "\nParaphrase:"
			restart_sequence = "\n\nArticle:"

			response = openai.Completion.create(
	  		engine="text-davinci-001",
	  		prompt="Article: Searching a specific search tree for a binary key can be programmed recursively or iteratively.\nParaphrase: Searching a specific search tree according to a binary key can be recursively or iteratively programmed.\n\nArticle: It was first released as a knapweed biocontrol in the 1980s in Oregon , and it is currently established in the Pacific Northwest.\nParaphrase: It was first released as Knopweed Biocontrol in Oregon in the 1980s , and is currently established in the Pacific Northwest.\n\nArticle: 4-OHT binds to ER , the ER / tamoxifen complex recruits other proteins known as co-repressors and then binds to DNA to modulate gene expression.\nParaphrase: The ER / Tamoxifen complex binds other proteins known as co-repressors and then binds to DNA to modulate gene expression.\n\nArticle: In mathematical astronomy, his fame is due to the introduction of the astronomical globe, and his early contributions to understanding the movement of the planets.\nParaphrase: His fame is due in mathematical astronomy to the introduction of the astronomical globe and to his early contributions to the understanding of the movement of the planets.\n\nArticle:Can I get a glass of water?\nParaphrase:May I have a glass of water?\n\nArticle:"+phrase+"\n",
	  		temperature=0.9,
	  		max_tokens=210,
	  		top_p=1,
	  		frequency_penalty=0,
	  		presence_penalty=0,
	  		stop=["\n\nArticle:", "\n"]
			)
			result = json.loads(str(response))
			answer = result["choices"][0]["text"]
			text.delete('1.0', tk.END)
			text.insert(tk.INSERT, answer)


		canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ccffff')
		canvas.pack(fill='both')

		frame = tk.Frame(root, bg='#1affff')
		frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

		entry= tk.Entry(frame, bg='white', font=15)
		entry.place(relx=0, rely=0.2, relwidth=0.8, relheight=0.1)

		label = tk.Label(frame, bg='#00cccc', text='Sentence for ParaPhrasing : ', font=18)
		label.place(relx=0, rely=0.1, relwidth=0.8, relheight=0.1)

		button = tk.Button(frame, bg='#00cccc', text='Submit', font=18, command=lambda:paraphrasinginterpretaion(entry.get()))
		button.place(relx=0.8, rely=0.097, relwidth=0.2, relheight=0.1)

		button = tk.Button(frame, bg='#00cccc', text='Clear', font=18, command=clear)
		button.place(relx=0.8, rely=0.2, relwidth=0.2, relheight=0.1)

		label = tk.Label(frame, bg='#00cccc', text='The PharaPhrased Senetence is : ', font=18)
		label.place(relx=0, rely=0.5, relwidth=1, relheight=0.1)

		text = tk.Text(frame, bg='white', font=18)
		text.place(relx=0, rely=0.6, relwidth=1, relheight=0.4)

		root.mainloop()



	########################################### Paraphrasing #################################################################


	########################################### IntentClassfication #########################################################

	def intentclassification():
		root=tk.Tk()

		def clear():
			entry.delete(0, tk.END)
			text.delete('1.0', tk.END)	

		def intent(intent):
			openai.api_key = "your-api-key"

			response = openai.Completion.create(
	  		engine="text-curie-001",
	  		prompt="listen to WestBam album allergic on google music: PlayMusic\ngive me a list of movie times for films in the area: SearchScreeningEvent\nshow me the picture creatures of light and darkness: SearchCreativeWork\nI would like to go to the popular bistro in oh: BookRestaurant\nwhat is the weather like in the city of Frewen in the country of Venezuela: GetWeather\nI want to book a flight for Kathmandu: BookFlight\nI want to play Football:SportsActivity\nLets do the classroom assignment:Educational Activity\n"+intent+":",
	  		temperature=0,
	  		max_tokens=10,
	  		top_p=1,
	  		frequency_penalty=0,
	  		presence_penalty=0,
	  		stop=["\n"]
			)
			result = json.loads(str(response))
			answer = result["choices"][0]["text"]
			text.delete('1.0', tk.END)
			text.insert(tk.INSERT, answer)


		canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#ccffff')
		canvas.pack(fill='both')

		label = tk.Label(root, bg='#00b3b3', text="Intent Finder", font=50)
		label.place(relx=0.0997, rely=0.1, relwidth=0.8, relheight=0.1)

		frame = tk.Frame(root, bg='#1affff')
		frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

		entry= tk.Entry(frame, bg='white', font=15)
		entry.place(relx=0, rely=0.2, relwidth=0.8, relheight=0.1)

		label = tk.Label(frame, bg='#00cccc', text='Statement for Intent classification: ', font=18)
		label.place(relx=0, rely=0.1, relwidth=0.8, relheight=0.1)

		button = tk.Button(frame, bg='#00cccc', text='Submit', font=18, command=lambda:intent(entry.get()))
		button.place(relx=0.8, rely=0.097, relwidth=0.2, relheight=0.1)

		button = tk.Button(frame, bg='#00cccc', text='Clear', font=18, command=clear)
		button.place(relx=0.8, rely=0.2, relwidth=0.2, relheight=0.1)

		label = tk.Label(frame, bg='#00cccc', text='The Intent of Statement is : ', font=18)
		label.place(relx=0, rely=0.5, relwidth=1, relheight=0.1)

		text = tk.Text(frame, bg='white', font=18)
		text.place(relx=0, rely=0.6, relwidth=1, relheight=0.4)

		root.mainloop()



	########################################### IntentClassfication #########################################################


	###################################################### main window #######################################################
	canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
	canvas.pack(fill='both')

	frame = tk.Frame(window, bg='#1affff')
	frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

	label = tk.Label(window, bg='#00b3b3', text="OpenAi - GPT3 Application", font=60)
	label.place(relx=0.0997, rely=0.1, relwidth=0.8, relheight=0.1)

	button = tk.Button(frame, text='QNA', bg='#00b3b3', fg='white', activebackground='white', font=40, command=qna)
	button.place(relx=0.1, rely=0.25, relwidth=0.3, relheight=0.1)

	button = tk.Button(frame, text='SQL Query', bg='#00b3b3', fg='white', activebackground='white', font=20, command=sqlquery)
	button.place(relx=0.6, rely=0.25, relwidth=0.3, relheight=0.1)

	button = tk.Button(frame, text='ParaPhrasing', bg='#00b3b3', fg='white', activebackground='white', font=40, command=paraphrasing)
	button.place(relx=0.1, rely=0.6, relwidth=0.3, relheight=0.1)

	button = tk.Button(frame, text='Intent Finder', bg='#00b3b3', fg='white', activebackground='white', font=40, command=intentclassification)
	button.place(relx=0.6, rely=0.6, relwidth=0.3, relheight=0.1)

	label = tk.Label(window, bg='#00b3b3', text="By - Suman, YogRaj , Sachit, Sangram", font=60)
	label.place(relx=0.0997, rely=0.8, relwidth=0.8, relheight=0.1)

	window.mainloop()

main() 
