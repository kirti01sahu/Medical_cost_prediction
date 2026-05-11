export default function MedicalCostPredictionUI() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6 font-sans">
      {/* Header */}
      <div className="bg-white rounded-3xl shadow-xl p-6 mb-6 flex flex-col md:flex-row justify-between items-center">
        <div>
          <h1 className="text-4xl font-bold text-indigo-700">Medical Cost Prediction System</h1>
          <p className="text-gray-600 mt-2 text-lg">
            AI-powered healthcare insurance charge prediction dashboard.
          </p>
        </div>

        <button className="mt-4 md:mt-0 bg-indigo-600 hover:bg-indigo-700 transition-all text-white px-6 py-3 rounded-2xl shadow-lg font-semibold">
          Predict Cost
        </button>
      </div>

      {/* Main Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Left Panel */}
        <div className="lg:col-span-1 bg-white rounded-3xl shadow-xl p-6">
          <h2 className="text-2xl font-bold text-gray-800 mb-5">Patient Information</h2>

          <div className="space-y-4">
            <input
              type="number"
              placeholder="Enter Age"
              className="w-full p-4 rounded-2xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"
            />

            <input
              type="number"
              placeholder="Enter BMI"
              className="w-full p-4 rounded-2xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"
            />

            <input
              type="number"
              placeholder="Number of Children"
              className="w-full p-4 rounded-2xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"
            />

            <select className="w-full p-4 rounded-2xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500">
              <option>Select Gender</option>
              <option>Male</option>
              <option>Female</option>
            </select>

            <select className="w-full p-4 rounded-2xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500">
              <option>Smoker?</option>
              <option>Yes</option>
              <option>No</option>
            </select>

            <select className="w-full p-4 rounded-2xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500">
              <option>Select Region</option>
              <option>Northwest</option>
              <option>Northeast</option>
              <option>Southeast</option>
              <option>Southwest</option>
            </select>

            <button className="w-full bg-green-600 hover:bg-green-700 transition-all text-white py-4 rounded-2xl text-lg font-semibold shadow-lg">
              Generate Prediction
            </button>
          </div>
        </div>

        {/* Right Panel */}
        <div className="lg:col-span-2 space-y-6">
          {/* Prediction Card */}
          <div className="bg-white rounded-3xl shadow-xl p-6">
            <h2 className="text-2xl font-bold text-gray-800 mb-4">Predicted Insurance Cost</h2>

            <div className="bg-gradient-to-r from-green-500 to-emerald-600 rounded-3xl p-8 text-white text-center shadow-lg">
              <p className="text-xl">Estimated Medical Cost</p>
              <h1 className="text-5xl font-bold mt-3">₹ 2,45,000</h1>
              <p className="mt-4 text-green-100">
                Prediction generated using Linear Regression Machine Learning Model.
              </p>
            </div>
          </div>

          {/* Analytics Section */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="bg-white rounded-3xl shadow-xl p-6">
              <h3 className="text-xl font-bold text-gray-800 mb-4">Model Accuracy</h3>

              <div className="flex items-center justify-center h-48">
                <div className="w-40 h-40 rounded-full border-[12px] border-indigo-600 flex items-center justify-center text-3xl font-bold text-indigo-700">
                  82%
                </div>
              </div>
            </div>

            <div className="bg-white rounded-3xl shadow-xl p-6">
              <h3 className="text-xl font-bold text-gray-800 mb-4">Project Insights</h3>

              <ul className="space-y-3 text-gray-600 text-lg">
                <li>✔ Predicts insurance charges using ML</li>
                <li>✔ Uses Linear Regression algorithm</li>
                <li>✔ Real-time patient data analysis</li>
                <li>✔ Visual dashboard for insights</li>
              </ul>
            </div>
          </div>

          {/* Graph Section */}
          <div className="bg-white rounded-3xl shadow-xl p-6">
            <h3 className="text-2xl font-bold text-gray-800 mb-6">Analytics Dashboard</h3>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="bg-indigo-100 rounded-2xl h-40 flex items-center justify-center text-indigo-700 font-bold text-xl">
                Age Distribution
              </div>

              <div className="bg-green-100 rounded-2xl h-40 flex items-center justify-center text-green-700 font-bold text-xl">
                BMI Analysis
              </div>

              <div className="bg-pink-100 rounded-2xl h-40 flex items-center justify-center text-pink-700 font-bold text-xl">
                Charges Histogram
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Footer */}
      <div className="mt-8 text-center text-gray-600 text-sm">
        Developed for AI-based Medical Insurance Cost Prediction using Machine Learning.
      </div>
    </div>
  );
}


========================================
*/
