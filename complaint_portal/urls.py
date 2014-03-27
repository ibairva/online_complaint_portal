from django.conf.urls import url,patterns

from complaint_portal import views

urlpatterns = patterns('',
	url(r'^index/',views.index,name="index"),
	url(r'^login/',views.login,name="login"),
	url(r'^activate/(?P<u_id>\d+)/',views.activate,name="activate"),
	url(r'^register/',views.register,name="register"),
	url(r'^logout/',views.logout,name="logout"),
	url(r'^ranking/',views.ranking,name="ranking"),
	url(r'^complainform/',views.complainform,name="complainform"),
	url(r'^all_complains',views.all_complains,name="all_complains"),
	url(r'^all_complains/(?P<loc_id>\d+)/',views.all_complains_location,name="views.all_complains_location"),
	url(r'^all_complains/(?P<complain_id>\d+)/details/',views.details,name="details"),
	url(r'^sorted_complains/(?P<sorted_id>\d+)/',views.sorted_complains,name="sorted_complains"),
	url(r'^userprofile/',views.userprofile,name="userprofile"),  
	url(r'^mycomplains/',views.mycomplains,name="mycomplains"),
	url(r'^profile_update/',views.profile_update,name="profile_update"),
	url(r'^complain_update/(?P<complain_id>\d+)/',views.complain_update,name="complain_update"),
	url(r'^(?P<complain_id>\d+)/complain_complete/',views.complain_complete,name="complain_complete"),
	url(r'^upvote/(?P<complain_id>\d+)/',views.upvote,name="upvote"),
	url(r'^middlemen/',views.middlemen,name="middlemen"),
	url(r'^middle/(?P<loc_id>\d+)/filter/',views.mloc_filter,name="mloc_filter"),
	url(r'^middlem/(?P<type_id>\d+)/filter/',views.mtype_filter,name="mtype_filter"),
	url(r'^mlogin/',views.mlogin,name="mlogin"),
	url(r'^mlogout/',views.mlogout,name="mlogout"),
	url(r'^forward_reject/',views.forward_reject,name="forward_reject"),
	url(r'^govtadmin/',views.govtadmin,name="govtadmin"),
	url(r'^glogin/',views.glogin,name="glogin"),
	url(r'^adminregister/',views.adminregister,name="adminregister"),
	) 

#updateform for each complain
#logout button as footer on each page
#a url and view when user clicks upvote button
#change password url and views
#see complainform_update.html give option of complete if it is accepted adn give option of update if it is not reviewed
#0-submitted,1-accept,2-reject,3-complete