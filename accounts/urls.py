from django.urls import path
from accounts.views import admin_login, admin_dashboard, admin_logout, school_setting, aboutus
from accounts.views import gallery_views 
from accounts.views import fees_views
from accounts.views import contact_views , facility_views
from accounts.views import slider_views
from accounts.views import admission_v
from accounts.views import license_views
from accounts.views import staff_views


urlpatterns = [
    path('api/admin/login/', admin_login),
    path('api/admin/dashboard/', admin_dashboard),
    path('api/admin/logout/', admin_logout),
    
    # ERP LICENSE
    path('api/erp/activate-license/', license_views.activate_license),
    path('api/erp/deactivate-license/',license_views.deactivate_license),
    path('api/erp/check-license-status/', license_views.check_license_status),  
    
    # SCHOOL SETTINGS APIs
    path('api/admin/school-settings/add/', school_setting.add_school_settings),
    path('api/school-settings/', school_setting.get_school_settings),
    path('api/admin/school-settings/update/', school_setting.update_school_settings),
    path('api/admin/school-settings/delete/', school_setting.delete_school_settings),
    
    # About_Us
    path('api/admin/about-us/', aboutus.about_us_get),
    path('api/admin/about-us/create/', aboutus.about_us_create),
    path('api/admin/about-us/update/<int:id>/', aboutus.about_us_update),
    path('api/admin/about-us/delete/<int:id>/', aboutus.about_us_delete),

    # CATEGORY
    path('api/admin/gallery/categories/', gallery_views.gallery_categories),
    path('api/admin/gallery/category/update/<int:id>/', gallery_views.update_category),
    path('api/admin/gallery/category/delete/<int:id>/', gallery_views.delete_category),

    # ALBUM
    path('api/admin/gallery/albums/', gallery_views.albums),
    path('api/admin/gallery/album/update/<int:id>/', gallery_views.update_album),
    path('api/admin/gallery/album/delete/<int:id>/', gallery_views.delete_album),

    # ALBUM IMAGES
    path('api/admin/gallery/album-image/create/', gallery_views.create_album_image),
    path('api/admin/gallery/album-image/delete/<int:id>/', gallery_views.delete_album_image),
    path('api/admin/gallery/album-images/<int:album_id>/',gallery_views.album_images),


    # SCHOOL CLASS ROUTES
    path('api/admin/classes/', fees_views.list_classes),
    path('api/admin/classes/create/', fees_views.create_class),
    path('api/admin/classes/update/<int:id>/', fees_views.update_class),
    path('api/admin/classes/delete/<int:id>/', fees_views.delete_class),

    # TERM ROUTES
    path('api/admin/terms/', fees_views.list_terms),
    path('api/admin/terms/create/', fees_views.create_term),
    path('api/admin/terms/update/<int:id>/', fees_views.update_term),
    path('api/admin/terms/delete/<int:id>/', fees_views.delete_term),

    # FEE HEADER ROUTES
    path('api/admin/headers/', fees_views.list_fee_headers),
    path('api/admin/headers/create/', fees_views.create_fee_header),
    path('api/admin/headers/update/<int:id>/', fees_views.update_fee_header),
    path('api/admin/headers/delete/<int:id>/', fees_views.delete_fee_header),

    # FEE STRUCTURE ROUTES
    path('api/admin/fee-structure/create/', fees_views.create_fee_structure),
    path('api/admin/fee-structure/', fees_views.get_fee_structure),
    
     # Add school contact
    path('api/admin/contact-info/add/', contact_views.add_school_contact),
    # Get contact info
    path('api/contact-info/', contact_views.contact_info),
    path('api/admin/contact/update/<int:id>/', contact_views.update_school_contact),
    path('api/admin/contact/delete/<int:id>/', contact_views.delete_school_contact),

    # Contact form submit
    path('api/contact/submit/add/', contact_views.contact_submit),
    # Contact messages list
    path('api/admin/contact/messages/', contact_views.contact_messages),
    path('api/admin/contact/messages/delete/<int:id>/', contact_views.delete_contact_message),
    path('api/admin/contact/messages/<int:id>/read/', contact_views.mark_message_read),
    
  # facilities
    path('api/admin/facilities/add/', facility_views.add_facility),
    path('api/admin/facilities/', facility_views.list_facilities),
    path('api/admin/facilities/update/<int:id>/', facility_views.update_facility),
    path('api/admin/facilities/delete/<int:id>/', facility_views.delete_facility),
    
    #slider
    
    path('api/admin/sliders/add/', slider_views.add_slider),
    path('api/sliders/', slider_views.list_sliders),
    path('api/admin/sliders/update/<int:id>/', slider_views.update_slider),
    path('api/admin/sliders/delete/<int:id>/', slider_views.update_slider),

    #admission
    path('api/admin/admission/add/', admission_v.add_admission),
    path('api/admin/admissions/', admission_v.list_admissions),
    path('api/admin/admission/delete/<int:id>/', admission_v.delete_admission),
    path('api/admin/admission/update/<int:id>/', admission_v.update_admission_status),
    
    # ROLE
    path('api/staff/roles/add/', staff_views.add_role),
    path('api/staff/roles/', staff_views.list_roles),
    path('api/staff/roles/update/<int:id>/', staff_views.update_role),
    path('api/staff/roles/delete/<int:id>/', staff_views.delete_role),

    # STAFF
    path('api/staff/add/', staff_views.add_staff),
    path('api/staff/', staff_views.list_staff),
    path('api/staff/<int:id>/', staff_views.get_staff),
    path('api/staff/update/<int:id>/', staff_views.update_staff),
    path('api/staff/delete/<int:id>/', staff_views.delete_staff),
    path('api/staff/status/<int:id>/', staff_views.toggle_staff_status),

    # ATTENDANCE
    path('api/staff/attendance/mark/', staff_views.mark_attendance),
    path('api/staff/attendance/', staff_views.list_attendance),
    path('api/staff/attendance/<int:staff_id>/', staff_views.staff_attendance),

    # LEAVE
    path('api/staff/leave/apply/', staff_views.apply_leave),
    path('api/staff/leave/', staff_views.list_leaves),
    path('api/staff/leave/update/<int:id>/', staff_views.update_leave_status),
]
    

