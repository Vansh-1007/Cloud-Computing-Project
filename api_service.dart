import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  final String baseUrl =   'https://81dd-203-129-246-110.ngrok-free.app';

 // ✅ Replace with your ngrok URL

  Future<String> getChatbotResponse(String message) async {
  final response = await http.post(
    Uri.parse('$baseUrl/chat'),
    headers: {"Content-Type": "application/json"},
    body: jsonEncode({
      "message": message
    }),
  );

  if (response.statusCode == 200) {
    return jsonDecode(response.body)['response'];
  } else {
    return "Error: ${response.statusCode}";
  }
}

}
