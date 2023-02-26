import 'package:flutter/material.dart';
import "./pages/home_page.dart"

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
    //! TODO: Project Name here
      title: 'Project Name',
      theme: ThemeData(
    //! TODO: Primary Color here
        primarySwatch: Colors.blue,
      ),
      home: const HomePage(),
    );
  }
}
