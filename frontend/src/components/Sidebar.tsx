import React from 'react'

export default function Sidebar(){
  return (
    <aside className="w-64 p-6 bg-[#021121] min-h-screen">
      <div className="mb-8">
        <div className="text-xl font-bold text-emerald-300">EcoTwin AI</div>
        <div className="text-sm text-slate-400">Sustainability Dashboard (MVP)</div>
      </div>
      <nav className="space-y-2">
        <a className="block px-3 py-2 rounded text-slate-200 bg-transparent hover:bg-[#08313b]" href="#">Dashboard</a>
        <a className="block px-3 py-2 rounded text-slate-200 bg-transparent hover:bg-[#08313b]" href="#">Warehouse</a>
        <a className="block px-3 py-2 rounded text-slate-200 bg-transparent hover:bg-[#08313b]" href="#">Solar</a>
        <a className="block px-3 py-2 rounded text-slate-200 bg-transparent hover:bg-[#08313b]" href="#">Assistant</a>
      </nav>
    </aside>
  )
}
