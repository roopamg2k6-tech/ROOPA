import React from 'react'
import Dashboard from './pages/Dashboard'
import Sidebar from './components/Sidebar'

export default function App(){
  return (
    <div className="min-h-screen bg-[#04102a] text-slate-100">
      <div className="flex">
        <Sidebar />
        <main className="flex-1 p-6">
          <h1 className="text-2xl font-semibold text-emerald-300">EcoTwin AI — Dashboard (MVP)</h1>
          <Dashboard />
        </main>
      </div>
    </div>
  )
}
