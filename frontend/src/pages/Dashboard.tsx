import React, { useEffect, useState } from 'react'
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts'

export default function Dashboard(){
  const [metrics, setMetrics] = useState<any>(null)

  useEffect(()=>{
    fetch('/api/solar')
      .then(r=>r.json())
      .then(setMetrics)
      .catch(()=>{})
  },[])

  const data = metrics ? [
    {name: 'Expected', value: metrics.expected_kw},
    {name: 'Actual', value: metrics.actual_kw},
    {name: 'Inverter', value: metrics.inverter_kw},
  ] : []

  return (
    <div className="mt-6 space-y-6">
      <div className="grid grid-cols-3 gap-4">
        <div className="p-4 bg-[#072033] rounded shadow">
          <div className="text-sm text-slate-400">Expected (kW)</div>
          <div className="text-2xl text-emerald-400">{metrics?.expected_kw ?? '—'}</div>
        </div>
        <div className="p-4 bg-[#072033] rounded shadow">
          <div className="text-sm text-slate-400">Actual (kW)</div>
          <div className="text-2xl text-emerald-400">{metrics?.actual_kw ?? '—'}</div>
        </div>
        <div className="p-4 bg-[#072033] rounded shadow">
          <div className="text-sm text-slate-400">Energy Cost (USD)</div>
          <div className="text-2xl text-emerald-400">{metrics?.energy_cost_usd ?? '—'}</div>
        </div>
      </div>

      <div className="p-4 bg-[#072033] rounded shadow h-64">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data}>
            <XAxis dataKey="name" stroke="#9bbfbc"/>
            <YAxis stroke="#9bbfbc"/>
            <Tooltip />
            <Line type="monotone" dataKey="value" stroke="#2dd4bf" strokeWidth={3} />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  )
}
