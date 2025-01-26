import React from 'react';
import { Sun, Moon, Bot, MessageSquare, Github, Shield, Zap, CheckCircle } from 'lucide-react';
import useTheme from './hooks/useTheme';
import useDiscordInvite from './hooks/useDiscordInvite';

function App() {
  const { theme, toggleTheme } = useTheme();
  const { inviteUrl, loading } = useDiscordInvite();

  return (
    <div className={`min-h-screen ${theme === 'dark' ? 'dark bg-gray-900' : 'bg-gray-50'}`}>
      {/* Navigation */}
      <nav className="fixed w-full backdrop-blur-md bg-white/70 dark:bg-gray-900/70 z-50">
        <div className="container mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <Bot className="w-8 h-8 text-indigo-600 dark:text-indigo-400" />
              <span className="text-xl font-bold dark:text-white">Assistant Bot</span>
            </div>
            <div className="flex items-center space-x-4">
              <button
                onClick={toggleTheme}
                className="p-2 rounded-lg hover:bg-gray-200 dark:hover:bg-gray-800"
                aria-label="Toggle theme"
              >
                {theme === 'dark' ? (
                  <Sun className="w-5 h-5 text-yellow-500" />
                ) : (
                  <Moon className="w-5 h-5 text-gray-600" />
                )}
              </button>
              <a
                href={inviteUrl}
                className={`flex items-center px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors ${loading ? 'opacity-50 cursor-not-allowed' : ''}`}
              >
                <MessageSquare className="w-5 h-5 mr-2" />
                Join Discord
              </a>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="pt-32 pb-20">
        <div className="container mx-auto px-6">
          <div className="text-center">
            <h1 className="text-5xl font-bold mb-6 dark:text-white">
              Streamline Your data processes
            </h1>
            <p className="text-xl text-gray-600 dark:text-gray-300 mb-8 max-w-2xl mx-auto">
              Automate any process with our powerful Assistant. Save time and ensure accuracy in your workflows.
            </p>
            <div className="flex justify-center space-x-4">
              <a
                href="mailto:ryan.price@tetratech.com"
                className={`px-8 py-3 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors flex items-center ${loading ? 'opacity-50 cursor-not-allowed' : ''}`}
              >
                <MessageSquare className="w-5 h-5 mr-2" />
                Contact Team
              </a>
              <a
                href="https://github.com/apptester2025/assistant-bot"
                className="px-8 py-3 bg-gray-200 dark:bg-gray-800 text-gray-900 dark:text-white rounded-lg hover:bg-gray-300 dark:hover:bg-gray-700 transition-colors flex items-center"
              >
                <Github className="w-5 h-5 mr-2" />
                View on GitHub
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-gray-100 dark:bg-gray-800">
        <div className="container mx-auto px-6">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white dark:bg-gray-700 p-8 rounded-xl shadow-lg">
              <Shield className="w-12 h-12 text-indigo-600 dark:text-indigo-400 mb-4" />
              <h3 className="text-xl font-bold mb-4 dark:text-white"> Automation</h3>
              <p className="text-gray-600 dark:text-gray-300">
                Automatically track and manage through Discord & GroupMe.
              </p>
            </div>
            <div className="bg-white dark:bg-gray-700 p-8 rounded-xl shadow-lg">
              <Zap className="w-12 h-12 text-indigo-600 dark:text-indigo-400 mb-4" />
              <h3 className="text-xl font-bold mb-4 dark:text-white">Real-time Updates</h3>
              <p className="text-gray-600 dark:text-gray-300">
                Get instant notifications and updates.
              </p>
            </div>
            <div className="bg-white dark:bg-gray-700 p-8 rounded-xl shadow-lg">
              <CheckCircle className="w-12 h-12 text-indigo-600 dark:text-indigo-400 mb-4" />
              <h3 className="text-xl font-bold mb-4 dark:text-white">Easy Integration</h3>
              <p className="text-gray-600 dark:text-gray-300">
                Simple setup process and seamless integration with your existing Discord or GroupMe server.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-8 dark:bg-gray-900">
        <div className="container mx-auto px-6">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <div className="flex items-center space-x-2 mb-4 md:mb-0">
              <Bot className="w-6 h-6 text-indigo-600 dark:text-indigo-400" />
              <span className="text-sm dark:text-white">© 2025 Assistant Bot</span>
            </div>
            <div className="flex space-x-6">
              <a href="https://github.com/ppdrmonitor/assistant-bot" className="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white">
                <Github className="w-6 h-6" />
              </a>
              <a href={inviteUrl} className="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white">
                <MessageSquare className="w-6 h-6" />
              </a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;