def save_feedback_service(request):
    # Here you would save the user feedback (database, file, etc.)
    print(f"User {request.user_id} rated {request.food_id} as {request.grade_by_user}")
    return True
