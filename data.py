import requests
import json
import pandas as pd 
import numpy as np 


headers = {
'authorization': "bearer <Token>"
}

account_id ='IEAB2Y3U'
pillars = ['IEAB2Y3UI4HGWWVD',  # BAnDS
			# 'IEAB2Y3UI4HGWW3S', # DA&G
			# 'IEAB2Y3UI4HGWXCS', # #BI&D
			'IEAB2Y3UI4HGWXGB', # CO&DO
			'IEAB2Y3UI4HGWYLZ', # Global IB
			'IEAB2Y3UI4HGWXIA', # Business Growth
			'IEAB2Y3UI4HGWXOA', # G&P
			# 'IEAB2Y3UI4HGWXWZ', 
			# 'IEAB2Y3UI4HGWX25'
			]

da_g_pillar_id = 'IEAB2Y3UI4HGWW3S'

exclude_project_id = [
				"IEAB2Y3UI4HGW4IK", #250 Data Alignment & Governance [Global IB Migration]
				"IEAB2Y3UI4HGW4U2", #270 Data Alignment & Governance [Growth & Profitability]
				"IEAB2Y3UI4HGW4PN", #260 Data Alignment & Governance [Business Growth (Partner Programs)]
				"IEAB2Y3UI4HGW4DG", #240 Data Alignment & Governance [Commercial Office & Deal Operations]
				"IEAB2Y3UI4HGW7ZL",
				"IEAB2Y3UI4HGW76C",
				"IEAB2Y3UI4HGXAGG",
				"IEAB2Y3UI4HGW7VF"
								]

BASE_URL = "https://www.wrike.com/api/v3/"


#########################
#########################
######### Users #########
#########################
#########################

user_url = BASE_URL + "/contacts"
# folder_fields = str(['customFields','customColumnIds'])

response_users = requests.get(user_url, headers=headers)
	# params={'fields':folder_fields})

data_users = response_users.json()

df_users =  pd.DataFrame.from_dict(data_users['data'])

df_users = df_users[['id','firstName','lastName']]
df_users = df_users.rename(index=str, columns={'id': "user_id"})

# df_users.to_csv('users.csv', index=False)


#########################
#########################
####### FOLDERS #########
#########################
#########################

folder_url = BASE_URL + "folders/"
folder_fields = str(['customFields','customColumnIds'])

response_folders = requests.get(folder_url, headers=headers, 
	params={'fields':folder_fields})

data_folders = response_folders.json()

df_folders = pd.DataFrame.from_dict(data_folders['data'])
df_folders = df_folders[['id','title','childIds']]


s = df_folders.apply(lambda x: pd.Series(x['childIds']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'childIds'
df_folders = df_folders.drop('childIds', axis=1).join(s)
df_folders = df_folders.merge(df_folders, left_on='childIds', right_on='id', how='left')
df_folders = df_folders.merge(df_folders, left_on='childIds_y', right_on='id_x', how='inner')

df_folders = df_folders.rename(index=str, 
	columns={'id_x_x':'pillar_id', 'title_x_x':'pillar_title', 'childIds_x_x':'pillar_childIds', 
	'id_y_x':'project_id', 'title_y_x':'project_title','childIds_y_x':'project_childIds', 
	'id_x_y':'job_id',
	'title_x_y':'job_title', 'childIds_x_y':'job_childIds'})

da_g_folder = df_folders[df_folders['pillar_id'] == da_g_pillar_id]
# da_g_folder = da_g_folder[da_g_folder.job_title.str.startswith(('2'))]


df_folders = df_folders[df_folders['pillar_id'].isin(pillars)]
df_folders = df_folders[~df_folders['project_id'].isin(exclude_project_id)]


# Get DA&G Folder Structure Separately
# We want to avoid Double Counting



#########################
#########################
######## Tasks ##########
#########################
#########################

task_url = BASE_URL + "folders/IEAB2Y3UI4HGWWVD/tasks" 
task_fields = str(['parentIds','customFields','superTaskIds','superParentIds','responsibleIds'])
appended_data = []

status_list = {
		'IEAB2Y3UJMALYQEA': 'Requested',
		'IEAB2Y3UJMALYQEK': 'Delayed',
		'IEAB2Y3UJMALYQEU': 'Work In Progress',
		'IEAB2Y3UJMALYQE6': 'Live/Active',
		'IEAB2Y3UJMALYQFI': 'Future',
		'IEAB2Y3UJMALYQEB': 'Completed',
		'IEAB2Y3UJMAOI7AT': 'Live/Active',
		'IEAB2Y3UJMALZS3K': 'Future',
		'IEAB2Y3UJMAL6HCE': 'Not Started',
		'IEAB2Y3UJMAL6HCO': 'On Hold',
		'IEAB2Y3UJMALYQFV': 'Rejected'
		}

for pillar in pillars:
	task_url = BASE_URL + "folders/" + pillar + "/tasks" 

	response = requests.get(task_url, 
		headers=headers,
		params={'fields':task_fields, 'descendants': True, 'subTasks': True}
		)

	temp_data_tasks = response.json()
	temp_df = pd.DataFrame.from_dict(temp_data_tasks['data'])
	
	appended_data.append(temp_df)

df_tasks = pd.concat(appended_data, ignore_index=True )

#########################
#########################
###### DA_G Tasks #######
#########################
#########################

# Get DA&G Tasks Separately
# We want to avoid Double Counting

task_da_g_url = BASE_URL + "folders/" + da_g_pillar_id + "/tasks" 
response_da_g = requests.get(task_da_g_url, 
		headers=headers,
		params={'fields':task_fields, 'descendants': True, 'subTasks': True}
		)
da_g_tasks = response_da_g.json()

df_da_g = pd.DataFrame.from_dict(da_g_tasks['data'])

df_da_g = df_da_g[['id','title','parentIds','superParentIds','customStatusId','responsibleIds']]

s = df_da_g.apply(lambda x: pd.Series(x['parentIds']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'parentIds'
df_da_g = df_da_g.drop('parentIds', axis=1).join(s)

s = df_da_g.apply(lambda x: pd.Series(x['superParentIds']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'superParentIds'
df_da_g = df_da_g.drop('superParentIds', axis=1).join(s)

s = df_da_g.apply(lambda x: pd.Series(x['responsibleIds']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'responsibleIds'
df_da_g = df_da_g.drop('responsibleIds', axis=1).join(s)


def replace_parentid(df):
	if df['parentIds'] == 'IEAB2Y3UI7777777':
		return df['superParentIds']
	else:
		return df['parentIds']

def current_status(df):
	return status_list[df['customStatusId']]

df_da_g['parentIds'] = df_da_g.apply(replace_parentid, axis=1)
df_da_g = df_da_g.drop_duplicates()
df_da_g['Current_status'] = df_da_g.apply(current_status, axis=1)



df_tasks = df_tasks[['id','title','parentIds','superParentIds','customStatusId','responsibleIds']]

s = df_tasks.apply(lambda x: pd.Series(x['parentIds']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'parentIds'
df_tasks = df_tasks.drop('parentIds', axis=1).join(s)

s = df_tasks.apply(lambda x: pd.Series(x['superParentIds']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'superParentIds'
df_tasks = df_tasks.drop('superParentIds', axis=1).join(s)

s = df_tasks.apply(lambda x: pd.Series(x['responsibleIds']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'responsibleIds'
df_tasks = df_tasks.drop('responsibleIds', axis=1).join(s)

df_tasks['parentIds'] = df_tasks.apply(replace_parentid, axis=1)
df_tasks = df_tasks.drop_duplicates()
df_tasks['Current_status'] = df_tasks.apply(current_status, axis=1)

#########################
#########################
####### WorkFlow ########
#########################
#########################


workflow_url = BASE_URL + "accounts/IEAB2Y3U/workflows"

response_workflow = requests.get(workflow_url, headers=headers)

data_workflow = response_workflow.json()

workflow_df = pd.DataFrame.from_dict(data_workflow['data'])

# workflow_df.to_csv('workflow.csv', index=False)


#########################
#########################
######## Combine ########
#########################
#########################
df_da_g_all  = da_g_folder.merge(df_da_g, left_on='job_id', right_on='parentIds', how='inner')
df_all = df_folders.merge(df_tasks, left_on='job_id', right_on='parentIds', how='inner')
df_all = pd.concat([df_all,df_da_g_all])
df_all = df_all.merge(df_users, left_on='responsibleIds', right_on='user_id', how='left')
df_all['full_name'] = df_all['firstName'] + ' ' + df_all['lastName']


df_tasks.to_csv('tasks.csv', index=False)
df_folders.to_csv('folders.csv',index=False)
df_all.to_csv('all.csv', index=False)

#########################
#########################
# #Task for every Pillars
#########################
#########################


L1 = df_all[['pillar_title','project_title', 'id', 'Current_status','full_name']]
# L1 = L1.groupby(['pillar_title']).count().reset_index(level=0)

L2 = df_all[['pillar_title','project_title', 'id', 'Current_status']]
# L2 = L1.groupby(['pillar_title']).count().reset_index(level=0)

x_data = L1['pillar_title'].tolist()
y_data = L1['id'].tolist()



