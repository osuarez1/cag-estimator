"""Static example data used for cache-augmented generation (CAG)."""

EXAMPLES: list[dict] = [
    # --- WEB DEVELOPMENT ---
    {
        "meeting_summary": "The client requested a full redesign and rebuild of their monolithic e-commerce website into a modern, responsive web application. Requirements include a product catalog, secure shopping cart, user profiles, and a robust admin dashboard.",
        "estimation": """
        ## Estimation: Modern E-Commerce Platform Rebuild

        ### Task Breakdown:
        1. UI/UX Design & Prototyping: 60 hours
        2. Frontend Development (React/Next.js): 120 hours
        3. Backend APIs & Database Architecture: 100 hours
        4. Stripe Payment Gateway Integration: 30 hours
        5. Admin Dashboard implementation: 50 hours
        6. Testing & QA: 40 hours

        **Total estimated: 400 hours**
        **Recommended team:** 2 Full-stack developers, 1 UI/UX Designer, 1 QA Tester
        **Estimated duration:** 10-12 weeks
        """
    },
    {
        "meeting_summary": "The client needs a B2B SaaS landing page focused on lead generation, integrated with a headless CMS for easy content updates by their marketing team.",
        "estimation": """
        ## Estimation: B2B SaaS Landing Page with CMS

        ### Task Breakdown:
        1. UI/UX Design: 30 hours
        2. Frontend Setup & Implementation (Astro/Tailwind): 50 hours
        3. Headless CMS Setup (Sanity/Contentful): 25 hours
        4. CRM & Form Integrations: 15 hours
        5. SEO Optimization & QA: 15 hours

        **Total estimated: 135 hours**
        **Recommended team:** 1 Frontend Developer, 1 UI/UX Designer
        **Estimated duration:** 3-4 weeks
        """
    },
    {
        "meeting_summary": "Client requires a real-time web portal for property management, allowing tenants to pay rent and submit maintenance requests, while landlords can track properties and revenue.",
        "estimation": """
        ## Estimation: Property Management Web Portal

        ### Task Breakdown:
        1. Wireframing & UI Design: 50 hours
        2. Tenant Portal Setup: 80 hours
        3. Landlord Dashboard & Analytics: 90 hours
        4. Payment Processing (ACH/Credit): 40 hours
        5. Notifications System (Email/SMS): 20 hours
        6. QA & UAT: 35 hours

        **Total estimated: 315 hours**
        **Recommended team:** 2 Full-stack developers, 1 Project Manager
        **Estimated duration:** 8-10 weeks
        """
    },
    {
        "meeting_summary": "A healthcare startup needs a HIPAA-compliant web application for booking telehealth appointments and managing patient records.",
        "estimation": """
        ## Estimation: HIPAA-Compliant Telehealth Web App

        ### Task Breakdown:
        1. Architecture & Security Compliance Planning: 40 hours
        2. UI/UX Design (Accessibility focused): 60 hours
        3. WebRTC Video Integration: 80 hours
        4. Patient & Doctor Portals: 120 hours
        5. EHR/EMR Integration: 90 hours
        6. Penetration Testing & QA: 60 hours

        **Total estimated: 450 hours**
        **Recommended team:** 2 Senior Backend Developers, 1 Frontend Developer, 1 Security Specialist
        **Estimated duration:** 12-14 weeks
        """
    },

    # --- FRONTEND DEVELOPMENT ---
    {
        "meeting_summary": "The client has an existing backend API but needs a completely new frontend built in Vue.js for their logistics tracking software.",
        "estimation": """
        ## Estimation: Vue.js Frontend for Logistics Software

        ### Task Breakdown:
        1. Component Library Setup: 30 hours
        2. Authentication & Route Guards: 20 hours
        3. Real-time Map Dashboard UI: 70 hours
        4. Reporting & Data Tables UI: 50 hours
        5. API Integration & State Management: 60 hours
        6. Cross-browser Testing: 25 hours

        **Total estimated: 255 hours**
        **Recommended team:** 2 Frontend Developers
        **Estimated duration:** 6-8 weeks
        """
    },
    {
        "meeting_summary": "Client wants to migrate their legacy jQuery financial dashboard to a modern React architecture to improve load times and maintainability.",
        "estimation": """
        ## Estimation: React Migration for Financial Dashboard

        ### Task Breakdown:
        1. Codebase Audit & Architecture Planning: 20 hours
        2. State Management Setup (Redux): 25 hours
        3. Component Refactoring: 100 hours
        4. Data Visualization (D3.js/Chart.js): 60 hours
        5. E2E Testing Integration: 40 hours

        **Total estimated: 245 hours**
        **Recommended team:** 2 Frontend Developers, 1 QA Engineer
        **Estimated duration:** 6-7 weeks
        """
    },
    {
        "meeting_summary": "Client needs a pixel-perfect, highly animated frontend implementation of a marketing site based on provided Figma designs.",
        "estimation": """
        ## Estimation: Interactive Marketing Frontend

        ### Task Breakdown:
        1. Project Setup & Asset Optimization: 10 hours
        2. HTML/CSS Layouts & Responsiveness: 40 hours
        3. Custom WebGL/Three.js Animations: 60 hours
        4. Scroll-triggered Interactions (GSAP): 30 hours
        5. Performance Auditing & QA: 20 hours

        **Total estimated: 160 hours**
        **Recommended team:** 1 Creative Frontend Developer
        **Estimated duration:** 4-5 weeks
        """
    },

    # --- BACKEND DEVELOPMENT ---
    {
        "meeting_summary": "Client requires a highly scalable REST API built in Node.js/Express to serve a mobile app, including user auth, social media feeds, and push notification triggers.",
        "estimation": """
        ## Estimation: Social Media App REST API

        ### Task Breakdown:
        1. Database Schema & Architecture Setup: 30 hours
        2. Auth (OAuth2 & JWT): 25 hours
        3. Feed Algorithm & CRUD Operations: 80 hours
        4. Push Notification Service (Firebase): 20 hours
        5. API Documentation (Swagger): 15 hours
        6. Unit & Integration Testing: 40 hours

        **Total estimated: 210 hours**
        **Recommended team:** 1 Senior Backend Developer
        **Estimated duration:** 5-7 weeks
        """
    },
    {
        "meeting_summary": "The company wants to extract their billing and invoicing module from their Ruby on Rails monolith into an independent Python FastAPI microservice.",
        "estimation": """
        ## Estimation: Billing Microservice Extraction

        ### Task Breakdown:
        1. Systems Analysis & Data Mapping: 40 hours
        2. FastAPI Setup & Boilerplate: 15 hours
        3. Core Billing Logic Implementation: 90 hours
        4. Database Migration Scripts: 50 hours
        5. Event Streaming Setup (Kafka): 35 hours
        6. Testing & CI/CD Pipeline Setup: 30 hours

        **Total estimated: 260 hours**
        **Recommended team:** 2 Backend Developers, 1 DevOps Engineer
        **Estimated duration:** 7-9 weeks
        """
    },
    {
        "meeting_summary": "Client needs a scalable WebSocket backend to handle real-time multiplayer state synchronization for a browser-based game.",
        "estimation": """
        ## Estimation: Multiplayer Game WebSocket Server

        ### Task Breakdown:
        1. Socket Server Architecture (Go/Node): 40 hours
        2. Room Management & Matchmaking: 50 hours
        3. State Synchronization Logic: 80 hours
        4. Anti-cheat Validation Middleware: 40 hours
        5. Load Testing & Optimization: 45 hours

        **Total estimated: 255 hours**
        **Recommended team:** 2 Backend Developers
        **Estimated duration:** 6-8 weeks
        """
    },

    # --- APPLE DEVELOPMENT ---
    {
        "meeting_summary": "The client wants a native iOS fitness application built with Swift and SwiftUI. It needs to integrate with Apple HealthKit, track GPS workouts, and display progress charts.",
        "estimation": """
        ## Estimation: Native iOS Fitness App

        ### Task Breakdown:
        1. UI/UX Design (iOS Human Interface Guidelines): 50 hours
        2. Core App Setup & Authentication: 30 hours
        3. HealthKit & Location Services Integration: 60 hours
        4. Workout Tracking & Offline Storage: 70 hours
        5. Charts & User Profile UI: 40 hours
        6. App Store Submission & QA: 25 hours

        **Total estimated: 275 hours**
        **Recommended team:** 1 iOS Developer, 1 UI/UX Designer
        **Estimated duration:** 7-9 weeks
        """
    },
    {
        "meeting_summary": "A restaurant needs a custom iPad POS (Point of Sale) app. It must connect to local thermal printers via Bluetooth, sync orders with a cloud backend, and support offline mode.",
        "estimation": """
        ## Estimation: iPad POS System

        ### Task Breakdown:
        1. UI/UX Design for iPad: 40 hours
        2. Core Order Management & Cart: 80 hours
        3. Offline Mode & CoreData Sync: 60 hours
        4. Bluetooth Printer Integration: 40 hours
        5. Payment Terminal SDK Integration: 35 hours
        6. QA & Hardware Testing: 45 hours

        **Total estimated: 300 hours**
        **Recommended team:** 2 iOS Developers
        **Estimated duration:** 8-10 weeks
        """
    },
    {
        "meeting_summary": "Client requires a macOS utility app that resides in the menu bar, monitors system CPU/RAM usage, and provides quick shortcuts to kill unresponsive tasks.",
        "estimation": """
        ## Estimation: macOS Menu Bar Utility

        ### Task Breakdown:
        1. App Architecture & Permissions: 20 hours
        2. System Resources Monitoring Logic: 35 hours
        3. Menu Bar UI Implementation (AppKit/SwiftUI): 25 hours
        4. Process Management Modules: 30 hours
        5. Testing on Intel/Apple Silicon: 15 hours

        **Total estimated: 125 hours**
        **Recommended team:** 1 macOS Developer
        **Estimated duration:** 3-4 weeks
        """
    },
    {
        "meeting_summary": "An existing iOS meditation app needs a companion Apple Watch application allowing users to start sessions, monitor heart rate during meditation, and save data.",
        "estimation": """
        ## Estimation: WatchOS Meditation Companion App

        ### Task Breakdown:
        1. WatchOS UI/UX Design: 20 hours
        2. WatchConnectivity Setup (iOS to Watch sync): 25 hours
        3. Session Player & Controls: 30 hours
        4. HealthKit Heart Rate Integration: 25 hours
        5. Standalone Mode Implementation: 20 hours
        6. Testing & QA: 15 hours

        **Total estimated: 135 hours**
        **Recommended team:** 1 iOS/WatchOS Developer
        **Estimated duration:** 3-4 weeks
        """
    },

    # --- ANDROID DEVELOPMENT ---
    {
        "meeting_summary": "Client needs a native Android e-learning app built in Kotlin. Users should be able to download video courses for offline viewing, take quizzes, and track progress.",
        "estimation": """
        ## Estimation: Native Android E-Learning App

        ### Task Breakdown:
        1. UI/UX Design (Material Design 3): 50 hours
        2. Authentication & User Profiles: 30 hours
        3. Video Player & DRM Implementation: 60 hours
        4. Offline Download Manager (WorkManager): 50 hours
        5. Quiz Engine & Progress Syncing: 45 hours
        6. QA & Play Store Submission: 30 hours

        **Total estimated: 265 hours**
        **Recommended team:** 1 Android Developer, 1 UI/UX Designer
        **Estimated duration:** 7-9 weeks
        """
    },
    {
        "meeting_summary": "Client has an existing legacy Java Android app and wants to fully migrate it to Kotlin using Jetpack Compose and an MVVM architecture.",
        "estimation": """
        ## Estimation: Android App Kotlin/Compose Migration

        ### Task Breakdown:
        1. Architecture Audit & Migration Strategy: 20 hours
        2. Domain & Data Layer Conversion to Kotlin: 60 hours
        3. UI Migration to Jetpack Compose: 100 hours
        4. Dependency Injection Update (Hilt): 20 hours
        5. Testing (Unit & UI Tests): 40 hours

        **Total estimated: 240 hours**
        **Recommended team:** 2 Android Developers
        **Estimated duration:** 6-8 weeks
        """
    },
    {
        "meeting_summary": "A logistics company needs a specialized Android app for enterprise inventory scanners. It requires deep integration with hardware barcode scanners and offline caching.",
        "estimation": """
        ## Estimation: Enterprise Android Inventory Scanner

        ### Task Breakdown:
        1. Hardware SDK Evaluation & Setup: 20 hours
        2. UI/UX Design for Rugged Devices: 30 hours
        3. Scanner Hardware Integration via Intent/SDK: 50 hours
        4. Local Database Setup (Room): 30 hours
        5. Sync Logic & Conflict Resolution: 40 hours
        6. Field Testing & UAT: 30 hours

        **Total estimated: 200 hours**
        **Recommended team:** 1 Android Developer
        **Estimated duration:** 5-7 weeks
        """
    },
    {
        "meeting_summary": "Client wants an Android TV app designed to stream their catalog of indie films. It needs a Leanback UI, video playback, and simple category navigation.",
        "estimation": """
        ## Estimation: Android TV Streaming App

        ### Task Breakdown:
        1. Android TV UI/UX Design: 30 hours
        2. Leanback Library Setup & Navigation: 40 hours
        3. ExoPlayer Integration: 35 hours
        4. API Integration (Catalog & Auth): 30 hours
        5. D-Pad Navigation Optimization: 20 hours
        6. QA on Physical Devices: 25 hours

        **Total estimated: 180 hours**
        **Recommended team:** 1 Android Developer
        **Estimated duration:** 4-6 weeks
        """
    },

    # --- ROKU DEVELOPMENT ---
    {
        "meeting_summary": "A media network wants to launch a VOD streaming channel on Roku using SceneGraph. It requires user authentication, video playback with ads (CSAI), and content categorization.",
        "estimation": """
        ## Estimation: Roku VOD Streaming Channel

        ### Task Breakdown:
        1. UI/UX Design for TV: 30 hours
        2. BrightScript/SceneGraph Project Setup: 40 hours
        3. Feed Parsing & Grid Setup: 50 hours
        4. Video Player & Ad SDK Integration: 60 hours
        5. User Authentication (Device Linking): 30 hours
        6. QA & Roku Certification Readiness: 40 hours

        **Total estimated: 250 hours**
        **Recommended team:** 1 Roku Developer, 1 QA Tester
        **Estimated duration:** 6-8 weeks
        """
    },
    {
        "meeting_summary": "Client needs a Live TV Roku app for broadcasting sports events. It needs to support HLS streams, a live EPG (Electronic Program Guide), and pay-per-view access.",
        "estimation": """
        ## Estimation: Roku Live TV & PPV App

        ### Task Breakdown:
        1. SceneGraph UI Setup: 30 hours
        2. EPG (Electronic Program Guide) UI & Data: 50 hours
        3. Live HLS Player Implementation: 40 hours
        4. Roku Pay / In-App Purchases Setup: 50 hours
        5. Analytics Integration: 20 hours
        6. QA & Performance Testing: 30 hours

        **Total estimated: 220 hours**
        **Recommended team:** 1 Roku Developer
        **Estimated duration:** 5-7 weeks
        """
    },
    {
        "meeting_summary": "A gaming studio wants to port a simple 2D casual game (trivia/puzzle) to the Roku platform with global leaderboards.",
        "estimation": """
        ## Estimation: Roku Casual Game Port

        ### Task Breakdown:
        1. BrightScript Game Loop Translation: 40 hours
        2. Remote Control Input Mapping: 20 hours
        3. 2D Rendering via SceneGraph: 60 hours
        4. API Integration for Leaderboards: 25 hours
        5. Audio Integration: 15 hours
        6. Roku Channel Store Submission: 20 hours

        **Total estimated: 180 hours**
        **Recommended team:** 1 Roku Developer
        **Estimated duration:** 4-6 weeks
        """
    },

    # --- SAMSUNG DEVELOPMENT (TIZEN) ---
    {
        "meeting_summary": "The client wants a Samsung Smart TV (Tizen) app for guided at-home workouts. It needs to display video routines, timers, and connect with a backend for user subscriptions.",
        "estimation": """
        ## Estimation: Samsung Tizen Fitness App

        ### Task Breakdown:
        1. Tizen Web App Setup & TV UI Design: 40 hours
        2. Navigation & Focus Management: 30 hours
        3. AVPlay Video Player Integration: 40 hours
        4. Workout Logic & On-screen Timers: 35 hours
        5. Samsung Checkout Integration: 45 hours
        6. QA & Tizen Store Submission: 30 hours

        **Total estimated: 220 hours**
        **Recommended team:** 1 Smart TV Developer
        **Estimated duration:** 5-7 weeks
        """
    },
    {
        "meeting_summary": "An educational company wants an interactive app for kids on Samsung TVs. It requires animations, simple remote interactions, and tracking completion of modules.",
        "estimation": """
        ## Estimation: Tizen Interactive Educational App

        ### Task Breakdown:
        1. UI/UX Design for Children: 30 hours
        2. HTML5/CSS/JS Animations Implementation: 60 hours
        3. Remote Control Interaction Logic: 25 hours
        4. State Management & Progress Tracking: 35 hours
        5. Sound Effects & Media Handling: 20 hours
        6. QA on Samsung Emulators & Devices: 25 hours

        **Total estimated: 195 hours**
        **Recommended team:** 1 Frontend/Smart TV Developer
        **Estimated duration:** 4-6 weeks
        """
    },
    {
        "meeting_summary": "Client needs a standard VOD media application for Samsung Smart TVs to expand their existing web platform reach. Requires DRM video playback.",
        "estimation": """
        ## Estimation: Samsung VOD Application

        ### Task Breakdown:
        1. Project Setup & Tizen SDK Configuration: 15 hours
        2. UI Layout & Remote Navigation: 40 hours
        3. Content API Integration: 30 hours
        4. AVPlay Integration with PlayReady/Widevine DRM: 60 hours
        5. Analytics & Error Logging: 20 hours
        6. Device QA & Certification: 30 hours

        **Total estimated: 195 hours**
        **Recommended team:** 1 Smart TV Developer
        **Estimated duration:** 5-6 weeks
        """
    },

    # --- LG DEVELOPMENT (webOS) ---
    {
        "meeting_summary": "Client requires an LG webOS application that acts as a dashboard for a smart home system. It needs to display camera feeds and control IoT devices via the Magic Remote.",
        "estimation": """
        ## Estimation: LG webOS Smart Home Dashboard

        ### Task Breakdown:
        1. webOS UI/UX Design (Enact Framework): 40 hours
        2. Magic Remote Pointer Integration: 20 hours
        3. Live Camera Feed (WebRTC/HLS): 60 hours
        4. IoT API Integration (Lights/Thermostat): 40 hours
        5. Background Services & Notifications: 30 hours
        6. QA on LG Devices: 30 hours

        **Total estimated: 220 hours**
        **Recommended team:** 1 Smart TV Developer
        **Estimated duration:** 5-7 weeks
        """
    },
    {
        "meeting_summary": "A news organization wants an LG TV app to show live news broadcasts, weather widgets, and scrolling text tickers.",
        "estimation": """
        ## Estimation: LG webOS News Aggregator

        ### Task Breakdown:
        1. UI/UX Design & Layouts: 30 hours
        2. Enact Framework Setup: 20 hours
        3. Live Stream Video Player Integration: 40 hours
        4. Weather & RSS Feed Parsers: 30 hours
        5. Ticker Animation Implementation: 20 hours
        6. LG Content Store Certification Readiness: 25 hours

        **Total estimated: 165 hours**
        **Recommended team:** 1 Smart TV Developer
        **Estimated duration:** 4-5 weeks
        """
    },
    {
        "meeting_summary": "A client wants to adapt their HTML5 web games to run smoothly on LG webOS TVs, requiring performance optimization and remote control mapping.",
        "estimation": """
        ## Estimation: LG webOS Game Portal

        ### Task Breakdown:
        1. HTML5 Canvas Optimization for TV: 40 hours
        2. Magic Remote & D-Pad Input Mapping: 30 hours
        3. Game Selection UI Integration: 30 hours
        4. Local Storage & High Scores: 15 hours
        5. Sound Optimization: 15 hours
        6. Performance QA across webOS versions: 25 hours

        **Total estimated: 155 hours**
        **Recommended team:** 1 Web/Game Developer
        **Estimated duration:** 4-5 weeks
        """
    },

    # --- AGENTIC DEVELOPMENT (AI) ---
    {
        "meeting_summary": "The client wants to build an autonomous AI customer support agent capable of resolving returns and issuing refunds by connecting an LLM to their Shopify backend.",
        "estimation": """
        ## Estimation: Autonomous Customer Support Agent

        ### Task Breakdown:
        1. Agent Architecture & Prompt Engineering: 40 hours
        2. Tool creation (Shopify API integration): 50 hours
        3. LangChain/LangGraph orchestration: 60 hours
        4. Guardrails & Safety Policy implementation: 30 hours
        5. Evaluation Framework (RAGAS/TruLens): 40 hours
        6. Human-in-the-loop Handoff Logic: 20 hours

        **Total estimated: 240 hours**
        **Recommended team:** 1 AI/ML Engineer, 1 Backend Developer
        **Estimated duration:** 6-8 weeks
        """
    },
    {
        "meeting_summary": "A law firm needs a multi-agent system where one agent researches case law (RAG), another drafts summaries, and a third acts as a critic to ensure legal accuracy before presenting to a human lawyer.",
        "estimation": """
        ## Estimation: Multi-Agent Legal Research System

        ### Task Breakdown:
        1. Vector Database Setup & RAG Pipeline: 60 hours
        2. Multi-Agent Orchestration (AutoGen/CrewAI): 50 hours
        3. System Prompts & Role Definition: 30 hours
        4. Critic Agent Validation Logic: 40 hours
        5. UI Dashboard for Lawyers: 40 hours
        6. Accuracy Evaluation & Tuning: 40 hours

        **Total estimated: 260 hours**
        **Recommended team:** 2 AI Engineers, 1 Frontend Developer
        **Estimated duration:** 7-9 weeks
        """
    },
    {
        "meeting_summary": "A software company wants an AI agent that automatically reads pull requests, identifies potential bugs, writes unit tests, and submits suggestions directly to GitHub.",
        "estimation": """
        ## Estimation: AI Software QA Agent

        ### Task Breakdown:
        1. GitHub App & Webhook Integration: 30 hours
        2. Code Parsing & Context Window Optimization: 40 hours
        3. LLM Code Generation & Test Writing Logic: 60 hours
        4. Sandboxed Execution Environment (Docker): 50 hours
        5. Automated PR Commenting System: 20 hours
        6. Testing & Security Auditing: 40 hours

        **Total estimated: 240 hours**
        **Recommended team:** 1 AI Engineer, 1 DevOps Engineer
        **Estimated duration:** 6-8 weeks
        """
    }
,

    # --- WEB DEVELOPMENT ---
    {
        "meeting_summary": "Client wants a niche crowdfunding web platform tailored for independent filmmakers. It requires project creation, tiered reward tiers, secure payment holding, and social sharing features.",
        "estimation": """
        ## Estimation: Niche Crowdfunding Platform

        ### Task Breakdown:
        1. UI/UX Design & User Flows: 70 hours
        2. Frontend Setup (Next.js): 100 hours
        3. Backend Architecture & Database: 90 hours
        4. Stripe Connect Integration (Escrow/Payouts): 60 hours
        5. Project Management & Reward Tier Logic: 50 hours
        6. QA & Security Auditing: 40 hours

        **Total estimated: 410 hours**
        **Recommended team:** 2 Full-stack developers, 1 UI/UX Designer
        **Estimated duration:** 10-12 weeks
        """
    },
    {
        "meeting_summary": "A regional restaurant chain needs a unified online reservation web app that syncs across their 15 locations, with an admin panel for hostesses to manage tables in real-time.",
        "estimation": """
        ## Estimation: Multi-Location Reservation System

        ### Task Breakdown:
        1. UI/UX Design (Customer & Admin views): 50 hours
        2. Database Design for multi-tenancy: 30 hours
        3. Customer Booking Interface (Frontend): 60 hours
        4. Hostess Admin Dashboard (Real-time updates): 80 hours
        5. Email/SMS Confirmation Service: 20 hours
        6. System Testing & Deployment: 30 hours

        **Total estimated: 270 hours**
        **Recommended team:** 2 Full-stack developers
        **Estimated duration:** 7-9 weeks
        """
    },
    {
        "meeting_summary": "Client requires a real estate listing aggregator. Needs a fast map-based search interface, property detail pages, and MLS data feed integration via API.",
        "estimation": """
        ## Estimation: Real Estate Map Aggregator

        ### Task Breakdown:
        1. Map UI Implementation (Mapbox/Google Maps): 60 hours
        2. MLS API Integration & Data Sync: 80 hours
        3. Property Detail Pages & Search Filters: 50 hours
        4. Favorite/Saved Search Functionality: 30 hours
        5. SEO Optimization (Server-side rendering): 20 hours
        6. QA & Cross-browser Testing: 30 hours

        **Total estimated: 270 hours**
        **Recommended team:** 1 Frontend Developer, 1 Backend Developer
        **Estimated duration:** 6-8 weeks
        """
    },
    {
        "meeting_summary": "A startup wants to launch a remote tech job board. Features include employer company profiles, job posting workflows with Stripe payments, and a candidate resume database.",
        "estimation": """
        ## Estimation: Remote Tech Job Board

        ### Task Breakdown:
        1. Wireframing & UI Design: 40 hours
        2. Employer & Candidate Auth flows: 30 hours
        3. Job Posting & Search Engine: 70 hours
        4. Stripe Integration for Job Listings: 20 hours
        5. Resume Upload & Parsing: 40 hours
        6. QA & Launch Prep: 25 hours

        **Total estimated: 225 hours**
        **Recommended team:** 2 Full-stack developers
        **Estimated duration:** 5-7 weeks
        """
    },

    # --- FRONTEND DEVELOPMENT ---
    {
        "meeting_summary": "Client wants to migrate their aging React-based corporate blog to SvelteKit for better performance and a smaller bundle size, keeping the exact same design.",
        "estimation": """
        ## Estimation: SvelteKit Blog Migration

        ### Task Breakdown:
        1. SvelteKit Project Initialization: 10 hours
        2. Layout & CSS Translation: 30 hours
        3. React Component to Svelte Translation: 60 hours
        4. Headless CMS API Re-integration: 25 hours
        5. SEO & Meta Tag configuration: 15 hours
        6. Performance Profiling & QA: 20 hours

        **Total estimated: 160 hours**
        **Recommended team:** 1 Frontend Developer
        **Estimated duration:** 4-5 weeks
        """
    },
    {
        "meeting_summary": "A company needs a frontend developer to build an internal knowledge base/wiki using an existing design system and Tailwind CSS, consuming a provided REST API.",
        "estimation": """
        ## Estimation: Internal Wiki Frontend

        ### Task Breakdown:
        1. Tailwind Configuration & Theming: 15 hours
        2. Navigation & Document Tree UI: 30 hours
        3. Markdown Editor Integration: 40 hours
        4. Search Interface Implementation: 25 hours
        5. API Wiring (CRUD articles): 30 hours
        6. UI Testing: 20 hours

        **Total estimated: 160 hours**
        **Recommended team:** 1 Frontend Developer
        **Estimated duration:** 4-5 weeks
        """
    },
    {
        "meeting_summary": "An automotive parts retailer needs a highly interactive 3D product configurator on their frontend using WebGL/Three.js to let users customize car rims.",
        "estimation": """
        ## Estimation: 3D Product Configurator

        ### Task Breakdown:
        1. 3D Model Optimization & Loading: 30 hours
        2. Three.js Scene Setup (Lighting/Cameras): 40 hours
        3. Material & Color Switching Logic: 50 hours
        4. UI Controls & React Integration: 40 hours
        5. Price Calculation Engine: 20 hours
        6. Mobile Performance Tuning: 30 hours

        **Total estimated: 210 hours**
        **Recommended team:** 1 WebGL Developer, 1 Frontend Developer
        **Estimated duration:** 6-7 weeks
        """
    },
    {
        "meeting_summary": "Client needs a complex, highly validated multi-step wizard form for a mortgage application process. Needs to save state locally in case of browser refresh.",
        "estimation": """
        ## Estimation: Complex Mortgage Application Wizard

        ### Task Breakdown:
        1. Form State Management Setup (Zustand/Redux): 20 hours
        2. Step-by-step UI Implementation: 40 hours
        3. Strict Field Validation (Zod/Yup): 30 hours
        4. LocalStorage State Persistence: 15 hours
        5. Document Upload UI (Drag & Drop): 25 hours
        6. QA & Edge-case Testing: 20 hours

        **Total estimated: 150 hours**
        **Recommended team:** 1 Frontend Developer
        **Estimated duration:** 4-5 weeks
        """
    },

    # --- BACKEND DEVELOPMENT ---
    {
        "meeting_summary": "The client has several legacy REST microservices and wants a unified GraphQL API gateway built to serve their new mobile and web applications efficiently.",
        "estimation": """
        ## Estimation: GraphQL API Gateway

        ### Task Breakdown:
        1. Architecture Planning & Schema Design: 40 hours
        2. Apollo Server Setup: 20 hours
        3. Resolvers & Data Source Wiring: 80 hours
        4. Caching & DataLoader Implementation: 30 hours
        5. Authentication & Rate Limiting: 25 hours
        6. Integration Testing: 30 hours

        **Total estimated: 225 hours**
        **Recommended team:** 1 Senior Backend Developer
        **Estimated duration:** 6-7 weeks
        """
    },
    {
        "meeting_summary": "A data analytics startup requires a heavy background processing pipeline built in Python with Celery to parse, clean, and store gigabytes of CSV uploads asynchronously.",
        "estimation": """
        ## Estimation: Asynchronous Data Processing Pipeline

        ### Task Breakdown:
        1. Celery/Redis Worker Setup: 20 hours
        2. File Ingestion & Chunking Logic: 40 hours
        3. Data Cleaning & Validation Rules: 60 hours
        4. Batch Database Insertion Optimization: 40 hours
        5. Progress Webhooks & Error Handling: 30 hours
        6. Load Testing: 20 hours

        **Total estimated: 210 hours**
        **Recommended team:** 1 Python Data Engineer
        **Estimated duration:** 5-6 weeks
        """
    },
    {
        "meeting_summary": "An e-commerce client is experiencing database bottleneck issues and needs a Redis caching layer implemented across their existing Node.js product catalog endpoints.",
        "estimation": """
        ## Estimation: Redis Caching Layer Implementation

        ### Task Breakdown:
        1. Codebase Audit & Bottleneck Identification: 15 hours
        2. Redis Cluster Setup & Configuration: 15 hours
        3. Cache Invalidation Strategy Design: 20 hours
        4. Implementation on Product Endpoints: 40 hours
        5. Fallback & Circuit Breaker Logic: 20 hours
        6. Performance Benchmarking & QA: 20 hours

        **Total estimated: 130 hours**
        **Recommended team:** 1 Backend Developer
        **Estimated duration:** 3-4 weeks
        """
    },
    {
        "meeting_summary": "Client needs an independent centralized notification microservice. It must expose APIs to trigger emails, SMS via Twilio, and push notifications, with queuing for high throughput.",
        "estimation": """
        ## Estimation: Centralized Notification Service

        ### Task Breakdown:
        1. Microservice Boilerplate & Database: 20 hours
        2. Message Queue Setup (RabbitMQ/SQS): 30 hours
        3. Email Provider Integration (SendGrid/AWS SES): 20 hours
        4. SMS & Push Notification Integrations: 30 hours
        5. Retry Logic & Dead Letter Queues: 25 hours
        6. Unit Testing & Documentation: 25 hours

        **Total estimated: 150 hours**
        **Recommended team:** 1 Backend Developer
        **Estimated duration:** 4-5 weeks
        """
    },

    # --- APPLE DEVELOPMENT ---
    {
        "meeting_summary": "A furniture retailer wants an iOS application featuring ARKit to allow customers to place 3D models of sofas and tables in their actual living rooms using their iPhone camera.",
        "estimation": """
        ## Estimation: ARKit Furniture Visualizer App

        ### Task Breakdown:
        1. iOS UI/UX App Design: 40 hours
        2. Product Catalog API Integration: 30 hours
        3. ARKit Scene Setup & Plane Detection: 60 hours
        4. 3D Model Loading & Manipulation Gestures: 50 hours
        5. Cart & Checkout Flow: 40 hours
        6. Device Testing & Optimization: 30 hours

        **Total estimated: 250 hours**
        **Recommended team:** 1 iOS Developer, 1 AR Specialist
        **Estimated duration:** 6-8 weeks
        """
    },
    {
        "meeting_summary": "Client requested a macOS native productivity utility built in AppKit/Swift that provides advanced keyboard shortcuts for snapping and managing open application windows.",
        "estimation": """
        ## Estimation: macOS Window Manager Utility

        ### Task Breakdown:
        1. Accessibility API Permissions Setup: 15 hours
        2. Keyboard Shortcut Listener Service: 20 hours
        3. Window Position Calculation Engine: 40 hours
        4. Preferences Menu Bar UI: 25 hours
        5. Multi-Monitor Support Logic: 30 hours
        6. Testing & Notarization: 15 hours

        **Total estimated: 145 hours**
        **Recommended team:** 1 macOS Developer
        **Estimated duration:** 4-5 weeks
        """
    },
    {
        "meeting_summary": "An independent media network wants an iOS app for their podcast network. Requires background audio playback, offline downloading, and Apple CarPlay support.",
        "estimation": """
        ## Estimation: iOS Podcast Application

        ### Task Breakdown:
        1. UI/UX Design: 40 hours
        2. RSS Parsing & Core Data Storage: 30 hours
        3. AVFoundation Background Audio Player: 50 hours
        4. Download Manager & Offline Mode: 40 hours
        5. Apple CarPlay Entitlements & UI: 40 hours
        6. QA & App Store Submission: 25 hours

        **Total estimated: 225 hours**
        **Recommended team:** 1 iOS Developer
        **Estimated duration:** 6-7 weeks
        """
    },

    # --- ANDROID DEVELOPMENT ---
    {
        "meeting_summary": "A ride-sharing startup needs an Android Automotive OS app built to run natively on compatible car dashboard screens, displaying maps, active rides, and earnings.",
        "estimation": """
        ## Estimation: Android Automotive Driver App

        ### Task Breakdown:
        1. Automotive OS Design Guidelines Review: 20 hours
        2. Car App Library Setup & Templates: 30 hours
        3. Map & Navigation Integration: 50 hours
        4. Backend Polling/Sockets for Ride Data: 40 hours
        5. Voice Interaction (Google Assistant): 30 hours
        6. Emulator & Hardware QA: 30 hours

        **Total estimated: 200 hours**
        **Recommended team:** 1 Android Developer
        **Estimated duration:** 5-7 weeks
        """
    },
    {
        "meeting_summary": "Client requires a native Android expense tracker that utilizes the device camera to scan physical receipts, extract text via OCR, and automatically categorize the expense.",
        "estimation": """
        ## Estimation: Android Expense Tracker with OCR

        ### Task Breakdown:
        1. Material Design UI implementation: 40 hours
        2. CameraX Integration & Image Cropping: 40 hours
        3. ML Kit OCR Integration for Text Extraction: 50 hours
        4. Expense Logic & Local Database (Room): 30 hours
        5. Cloud Syncing Service: 30 hours
        6. Testing & Bug Fixing: 25 hours

        **Total estimated: 215 hours**
        **Recommended team:** 1 Android Developer
        **Estimated duration:** 5-6 weeks
        """
    },
    {
        "meeting_summary": "An existing Android weather application needs a comprehensive suite of modern Home Screen widgets (Glance API) showing current conditions, hourly forecasts, and radar.",
        "estimation": """
        ## Estimation: Android Glance Weather Widgets

        ### Task Breakdown:
        1. Widget UI/UX Design: 20 hours
        2. Jetpack Glance Setup & Architecture: 15 hours
        3. Data Syncing (WorkManager) for Widgets: 25 hours
        4. Current Conditions & Forecast Widget: 30 hours
        5. Interactive Radar Widget Configuration: 25 hours
        6. Testing Across Android Versions: 20 hours

        **Total estimated: 135 hours**
        **Recommended team:** 1 Android Developer
        **Estimated duration:** 3-4 weeks
        """
    },

    # --- ROKU DEVELOPMENT ---
    {
        "meeting_summary": "A niche distributor of classic anime wants a standalone Roku channel. They have an existing REST API for their catalog. Features include watchlists and auto-play next episode.",
        "estimation": """
        ## Estimation: Anime Streaming Roku Channel

        ### Task Breakdown:
        1. SceneGraph UI Layout & Theming: 30 hours
        2. API Integration (Categories, Details): 40 hours
        3. Video Player Setup & Binge-watching Logic: 40 hours
        4. Watchlist & Continue Watching Sync: 30 hours
        5. Analytics & Ad-Tracking integration: 20 hours
        6. QA & Roku Certification: 30 hours

        **Total estimated: 190 hours**
        **Recommended team:** 1 Roku Developer
        **Estimated duration:** 5-6 weeks
        """
    },
    {
        "meeting_summary": "Client wants to build a premium Roku screensaver application that displays high-quality dynamic landscapes, digital clocks, and live local weather updates.",
        "estimation": """
        ## Estimation: Dynamic Roku Screensaver

        ### Task Breakdown:
        1. Screensaver Application Setup: 10 hours
        2. High-Res Image Cycling Logic: 20 hours
        3. Weather API Integration & Caching: 20 hours
        4. Custom Clock/Weather UI Overlay: 25 hours
        5. Settings Page (zip code, preferences): 20 hours
        6. Memory Leak Profiling & Testing: 15 hours

        **Total estimated: 110 hours**
        **Recommended team:** 1 Roku Developer
        **Estimated duration:** 3-4 weeks
        """
    },
    {
        "meeting_summary": "A large local mega-church wants a simple Roku application for their congregation to tune into live Sunday broadcasts and browse a VOD archive of past sermons.",
        "estimation": """
        ## Estimation: Church Live Stream & VOD Roku App

        ### Task Breakdown:
        1. UI Customization (Direct Publisher Customization): 20 hours
        2. Live HLS Stream Integration: 20 hours
        3. VOD Feed Setup (JSON parsing): 25 hours
        4. Category Navigation (By Series/Date): 15 hours
        5. Roku Deployment & Publishing: 15 hours

        **Total estimated: 95 hours**
        **Recommended team:** 1 Roku Developer
        **Estimated duration:** 2-3 weeks
        """
    },

    # --- SAMSUNG DEVELOPMENT (TIZEN) ---
    {
        "meeting_summary": "A retail brand wants a Tizen web app to run on Samsung commercial displays in their stores. It needs to loop promotional videos, display ticker text, and be remotely updatable.",
        "estimation": """
        ## Estimation: Tizen Digital Signage App

        ### Task Breakdown:
        1. Tizen Web Platform Setup: 15 hours
        2. Video Looping & Caching Logic: 35 hours
        3. Remote Polling API (Fetch new content): 25 hours
        4. HTML5 Ticker Overlay Implementation: 20 hours
        5. Auto-start & Crash Recovery Logic: 15 hours
        6. On-Site Hardware Testing: 20 hours

        **Total estimated: 130 hours**
        **Recommended team:** 1 Smart TV Developer
        **Estimated duration:** 3-4 weeks
        """
    },
    {
        "meeting_summary": "An art museum wants a premium Samsung Frame TV application that allows subscribers to cycle through high-resolution curated paintings, mimicking a physical canvas.",
        "estimation": """
        ## Estimation: Samsung TV Art Gallery App

        ### Task Breakdown:
        1. High-Fidelity UI Layout Design: 25 hours
        2. Tizen Image Rendering Optimization: 40 hours
        3. Subscription API & Auth Integration: 30 hours
        4. Custom Transitions & Slideshow Logic: 25 hours
        5. Ambient Mode Compatibility: 20 hours
        6. QA on Physical TV Hardware: 20 hours

        **Total estimated: 160 hours**
        **Recommended team:** 1 Smart TV Developer
        **Estimated duration:** 4-5 weeks
        """
    },
    {
        "meeting_summary": "Client wants to port their family organizer app specifically to Samsung Family Hub Smart Refrigerators running Tizen. Features include a shared calendar and grocery lists.",
        "estimation": """
        ## Estimation: Samsung Refrigerator Organizer App

        ### Task Breakdown:
        1. Family Hub UI Guidelines Review & Design: 30 hours
        2. Calendar Grid UI & Syncing: 50 hours
        3. Real-time Grocery List (WebSockets): 40 hours
        4. Touch Interaction Optimization: 20 hours
        5. Push Notifications for Reminders: 20 hours
        6. Tizen Store Certification: 25 hours

        **Total estimated: 185 hours**
        **Recommended team:** 1 Smart TV Developer
        **Estimated duration:** 5-6 weeks
        """
    },

    # --- LG DEVELOPMENT (webOS) ---
    {
        "meeting_summary": "A hotel chain requires a customized LG webOS app for their guest rooms. It must welcome the guest by name, offer room service menus, and provide a portal to Netflix/Hulu.",
        "estimation": """
        ## Estimation: LG webOS Hotel Hospitality App

        ### Task Breakdown:
        1. webOS UI Design (Hotel Branding): 30 hours
        2. Property Management System (PMS) API Integration: 40 hours
        3. Room Service Ordering Flow: 50 hours
        4. App Launcher Links (Deep linking to Netflix): 15 hours
        5. Auto-wipe User Data on Checkout Logic: 20 hours
        6. Field Testing at Hotel Location: 25 hours

        **Total estimated: 180 hours**
        **Recommended team:** 1 Smart TV Developer, 1 Backend Integration Eng.
        **Estimated duration:** 5-6 weeks
        """
    },
    {
        "meeting_summary": "A teleshopping network wants an interactive LG webOS app where viewers can watch the live broadcast and purchase the currently displayed item via their Magic Remote without calling.",
        "estimation": """
        ## Estimation: Interactive TV Shopping App

        ### Task Breakdown:
        1. Live Broadcast Integration (HLS): 20 hours
        2. Real-time Overlay UI (Current Item Specs): 40 hours
        3. E-commerce API & User Auth Integration: 50 hours
        4. Magic Remote One-Click Buy Flow: 30 hours
        5. Payment Gateway Tokenization Security: 30 hours
        6. Load Testing & QA: 25 hours

        **Total estimated: 195 hours**
        **Recommended team:** 1 Smart TV Developer
        **Estimated duration:** 5-6 weeks
        """
    },
    {
        "meeting_summary": "Client wants an LG webOS Karaoke application. Needs to play instrumental audio tracks while displaying perfectly synchronized scrolling lyrics highlighting the current word.",
        "estimation": """
        ## Estimation: LG webOS Karaoke App

        ### Task Breakdown:
        1. WebOS App Architecture & Layout: 20 hours
        2. Audio Player Integration: 20 hours
        3. LRC (Lyric) File Parsing Engine: 40 hours
        4. Hardware-Accelerated UI Animation (Lyrics sync): 50 hours
        5. Catalog Browsing & Search: 30 hours
        6. QA & Performance Tuning: 25 hours

        **Total estimated: 185 hours**
        **Recommended team:** 1 Frontend/TV Developer
        **Estimated duration:** 5-6 weeks
        """
    },

    # --- AGENTIC DEVELOPMENT (AI) ---
    {
        "meeting_summary": "A marketing agency wants an AI agent that automatically monitors industry news, generates a weekly social media content calendar, creates the post copy, and schedules them via Buffer.",
        "estimation": """
        ## Estimation: Autonomous Social Media Agent

        ### Task Breakdown:
        1. Web Scraping & RSS Feed Tooling: 30 hours
        2. LLM Prompt Engineering for Tone/Copywriting: 40 hours
        3. Agent Orchestration (LangChain): 40 hours
        4. Buffer API Integration (Scheduling tool): 25 hours
        5. Approval Dashboard UI (Human-in-the-loop): 30 hours
        6. Testing & Prompt Refinement: 20 hours

        **Total estimated: 185 hours**
        **Recommended team:** 1 AI Engineer, 1 Full-stack Developer
        **Estimated duration:** 5-6 weeks
        """
    },
    {
        "meeting_summary": "An accounting firm needs a specialized AI agent workflow to extract structured financial data (totals, dates, line items, taxes) from highly unstructured scanned PDF receipts and invoices.",
        "estimation": """
        ## Estimation: Document Extraction AI Agent

        ### Task Breakdown:
        1. OCR & Vision Model Setup (GPT-4V / Claude 3): 40 hours
        2. Information Extraction Prompting & JSON enforcing: 50 hours
        3. Fallback logic and Confidence Scoring: 30 hours
        4. ERP API Integration (QuickBooks/Xero): 30 hours
        5. Batch Processing Queue System: 30 hours
        6. Accuracy Benchmarking & Fine-tuning: 40 hours

        **Total estimated: 220 hours**
        **Recommended team:** 1 AI Engineer, 1 Backend Developer
        **Estimated duration:** 6-7 weeks
        """
    },
    {
        "meeting_summary": "An ed-tech company wants a conversational AI tutor agent that tests students on Python programming, evaluates their code in a sandbox, and dynamically adjusts the curriculum difficulty based on success.",
        "estimation": """
        ## Estimation: Dynamic AI Programming Tutor

        ### Task Breakdown:
        1. Conversational Agent Setup & Memory Management: 40 hours
        2. Secure Code Execution Sandbox (Docker API): 60 hours
        3. Curriculum State Machine Logic: 50 hours
        4. LLM Evaluation of User Code approach: 40 hours
        5. Frontend Chat Interface Integration: 30 hours
        6. Safety, Jailbreak Prevention & QA: 40 hours

        **Total estimated: 260 hours**
        **Recommended team:** 1 AI Engineer, 1 Backend Developer
        **Estimated duration:** 7-9 weeks
        """
    }
]
